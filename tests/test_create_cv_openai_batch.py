import sys
import importlib
import types
from pathlib import Path
from io import BytesIO
import zipfile

import pytest
from PyPDF2 import PdfReader
from unittest.mock import MagicMock


def streamlit_stub():
    import types
    st_stub = types.ModuleType("streamlit")
    st_stub.selectbox_calls = []

    def title(*args, **kwargs):
        pass

    def markdown(*args, **kwargs):
        pass

    def text_input(label, value="", **kwargs):
        return value

    def selectbox(label, options, index=0, **kwargs):
        st_stub.selectbox_calls.append({"label": label, "options": options, "index": index})
        return options[index]

    def number_input(label, min_value=None, max_value=None, value=0, **kwargs):
        return value

    def button(*args, **kwargs):
        return False

    def subheader(*args, **kwargs):
        pass

    def text_area(*args, **kwargs):
        pass

    def text(*args, **kwargs):
        pass

    def spinner(*args, **kwargs):
        from contextlib import nullcontext
        return nullcontext()

    def download_button(*args, **kwargs):
        pass

    def warning(*args, **kwargs):
        pass

    def error(*args, **kwargs):
        pass

    st_stub.title = title
    st_stub.markdown = markdown
    st_stub.text_input = text_input
    st_stub.selectbox = selectbox
    st_stub.number_input = number_input
    st_stub.button = button
    st_stub.subheader = subheader
    st_stub.text_area = text_area
    st_stub.text = text
    st_stub.spinner = spinner
    st_stub.download_button = download_button
    st_stub.warning = warning
    st_stub.error = error
    return st_stub


@pytest.fixture
def mock_streamlit(monkeypatch):
    st_stub = streamlit_stub()
    monkeypatch.setitem(sys.modules, "streamlit", st_stub)
    return st_stub


@pytest.fixture
def create_cv_openai_module(mock_streamlit, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1]))
    if "create_cv_openai_batch" in sys.modules:
        del sys.modules["create_cv_openai_batch"]
    return importlib.import_module("create_cv_openai_batch")


def test_generate_cvs_batch_calls_api(create_cv_openai_module, monkeypatch):
    expected_content = "Batch CV"
    mock_response = types.SimpleNamespace(
        choices=[types.SimpleNamespace(message={"content": expected_content})]
    )
    mock_create = MagicMock(return_value=mock_response)
    monkeypatch.setattr(
        create_cv_openai_module.openai.ChatCompletion, "create", mock_create
    )

    roles = ["Engineer", "Designer"]
    names = ["Alice", "Bob"]
    emails = ["a@example.com", "b@example.com"]
    phones = ["123", "456"]
    locations = ["City1", "City2"]
    exps = ["High", "Low"]

    responses = create_cv_openai_module.generate_cvs_batch(
        roles, names, emails, phones, locations, exps
    )

    assert responses == [expected_content, expected_content]
    assert mock_create.call_count == 2


def test_save_cv_as_pdf_creates_valid_pdf(create_cv_openai_module, tmp_path):
    file_path = tmp_path / "cv.pdf"
    sample_content = "Experience:\n5 years"
    create_cv_openai_module.save_cv_as_pdf(sample_content, str(file_path))

    assert file_path.exists()
    assert file_path.read_bytes().startswith(b"%PDF")
    reader = PdfReader(str(file_path))
    text = "\n".join(page.extract_text() for page in reader.pages)
    assert "Experience" in text


def test_delete_old_pdfs_removes_pdfs(create_cv_openai_module, tmp_path, monkeypatch):
    pdf1 = tmp_path / "old1.pdf"
    pdf2 = tmp_path / "old2.pdf"
    pdf1.write_text("dummy")
    pdf2.write_text("dummy")

    monkeypatch.chdir(tmp_path)
    create_cv_openai_module.delete_old_pdfs()
    assert list(tmp_path.glob("*.pdf")) == []


def test_job_roles_length(create_cv_openai_module):
    assert len(create_cv_openai_module.job_roles) >= 60, "job_roles should contain at least 60 entries"


def test_experience_level_options(create_cv_openai_module, mock_streamlit):
    assert mock_streamlit.selectbox_calls[0]["options"] == ["High", "Low", "Random"]
    assert mock_streamlit.selectbox_calls[0]["index"] == 2
    assert create_cv_openai_module.experience_level == "Random"


def test_zip_packaging(create_cv_openai_module, tmp_path):
    file1 = tmp_path / "cv1.pdf"
    file2 = tmp_path / "cv2.pdf"
    create_cv_openai_module.save_cv_as_pdf("test", str(file1))
    create_cv_openai_module.save_cv_as_pdf("test", str(file2))

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        zip_file.write(str(file1), arcname=file1.name)
        zip_file.write(str(file2), arcname=file2.name)

    zip_buffer.seek(0)
    with zipfile.ZipFile(zip_buffer) as z:
        assert set(z.namelist()) == {file1.name, file2.name}

