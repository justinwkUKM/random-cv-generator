import os
import streamlit as st
import openai
import random
from fpdf import FPDF
from dotenv import load_dotenv
import faker
import zipfile
from io import BytesIO
import glob

# Load environment variables from a .env file
load_dotenv()

# Set up the OpenAI client with API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Streamlit App
st.title("🌟 Random CV Generator")

# Application description and instructions
st.markdown(
    """
    ### Welcome to the Random CV Generator!
    This application allows you to generate customized CVs for different job roles in just a few clicks. 🚀
    
    **How to Use:**
    - Select the job role for which you want to generate CVs.
    - Specify the location and experience level of the candidates.
    - Generate multiple CVs at once, and download them in a ZIP file.
    
    **Why Use This Tool?**
    - Quickly create tailored CVs for testing, prototyping, or HR use.
    - Save time by generating realistic CVs with relevant skills and experiences.
    
    """
)
st.markdown("---")

# Input form for the job role and other details
location = st.text_input("🌍 Enter the location:", value="Saudi Arabia")
experience_level = st.selectbox("🔧 Select the experience level:", ["High", "Low", "Random"], index=2)
num_cvs = st.number_input("📄 Enter the number of CVs to generate:", min_value=1, max_value=50, value=5)

# List of common job roles to choose from
job_roles = [
    "Software Engineer", "Data Scientist", "Product Manager", "Project Coordinator", "Marketing Specialist",
    "Sales Executive", "Financial Analyst", "Human Resources Manager", "Graphic Designer", "Content Writer",
    "Customer Service Representative", "Business Analyst", "Accountant", "UX/UI Designer", "Network Administrator",
    "IT Support Specialist", "Operations Manager", "Administrative Assistant", "Legal Advisor", "Quality Assurance Tester",
    "Mechanical Engineer", "Electrical Engineer", "Civil Engineer", "Biomedical Engineer", "Chemical Engineer",
    "Systems Analyst", "Database Administrator", "DevOps Engineer", "Full Stack Developer", "Backend Developer",
    "Frontend Developer", "Cloud Architect", "Machine Learning Engineer", "AI Researcher", "Cybersecurity Specialist",
    "SEO Specialist", "Content Strategist", "Social Media Manager", "Public Relations Specialist", "Event Planner",
    "Supply Chain Manager", "Procurement Specialist", "Warehouse Manager", "Retail Store Manager", "Fitness Trainer",
    "Nutritionist", "Psychologist", "Teacher", "School Principal", "Professor", "Research Scientist", "Lab Technician",
    "Nurse", "Doctor", "Paramedic", "Pharmacist", "Veterinarian"
]
job_role = st.selectbox("💼 Select the job role:", job_roles)

def generate_cvs_batch(roles, names, emails, phone_numbers, locations, experience_levels):
    """
    Function to generate multiple CVs using OpenAI's Batch API
    """
    messages = [
        {
            "role": "user",
            "content": (
                f"Generate a CV for the role of {role}.\n"
                f"Location: {location}\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone Number: {phone_number}\n"
                f"Years of Experience: value should be an integer number based on {experience_level} number of years\n"
            )
        }
        for role, name, email, phone_number, location, experience_level in zip(roles, names, emails, phone_numbers, locations, experience_levels)
    ]

    # Generate each CV sequentially
    responses = []
    for message in messages:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[message],
            )
            responses.append(response.choices[0].message["content"])
        except Exception as e:
            responses.append(f"Error generating CV: {e}")
    return responses

def save_cv_as_pdf(cv_content, filename):
    """
    Function to save CV content to a PDF file with improved formatting
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title section of the PDF
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(0, 102, 204)  # Blue color for title
    pdf.cell(0, 10, "Curriculum Vitae", ln=True, align='C')
    pdf.ln(10)

    # Add a decorative line below the title
    pdf.set_draw_color(0, 102, 204)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)

    # Content Sections
    sections = cv_content.split('\n')
    current_section = ""
    for line in sections:
        if line.endswith(":"):
            # New section heading detected
            current_section = line.strip()
            pdf.set_font("Arial", 'B', 12)
            pdf.set_text_color(0, 51, 102)  # Dark blue color for section headings
            pdf.cell(0, 10, current_section, ln=True)
            pdf.set_font("Arial", size=12)
            pdf.set_text_color(0, 0, 0)  # Reset color to black for content
        else:
            # Content under the current section
            pdf.multi_cell(0, 10, line.strip())
        pdf.ln(5)

    # Save the PDF to the given filename
    pdf.output(filename)

def delete_old_pdfs():
    """
    Function to delete all old PDF files in the current working directory
    """
    old_pdfs = glob.glob("*.pdf")
    for pdf in old_pdfs:
        try:
            os.remove(pdf)
        except Exception as e:
            st.warning(f"Could not delete {pdf}: {e}")

# Generate CVs button
if st.button("✨ Generate Random CVs"):
    # Delete old PDF files before generating new ones
    delete_old_pdfs()
    if job_role:
        with st.spinner('⏳ Generating CVs, please wait...'):
            random_hashes = [str(random.randint(1000, 9999)) for _ in range(num_cvs)]  # Generate random hashes for email uniqueness
            fake = faker.Faker()
            random_names = [fake.name() for _ in range(num_cvs)]  # Generate random names
            random_emails = [f"{name.replace(' ', '.').lower()}{hash_}@example.com" for name, hash_ in zip(random_names, random_hashes)]  # Generate random emails
            random_phone_numbers = [fake.phone_number() for _ in range(num_cvs)]  # Generate random phone numbers
            random_locations = [location for _ in range(num_cvs)]  # Use the specified location for all CVs
            experience_levels = [experience_level for _ in range(num_cvs)]  # Use the specified experience level for all CVs
            
            # Generate the CV content using the OpenAI Batch API
            generated_cvs = generate_cvs_batch(
                roles=[job_role] * num_cvs,
                names=random_names,
                emails=random_emails,
                phone_numbers=random_phone_numbers,
                locations=random_locations,
                experience_levels=experience_levels
            )
            
            # Create a ZIP file to download all CVs
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                for idx, cv in enumerate(generated_cvs):
                    filename = f"cv_{job_role}_{idx + 1}_{random_names[idx].replace(' ', '_')}.pdf"
                    save_cv_as_pdf(cv, filename)
                    st.subheader(f"CV {idx + 1} of {num_cvs}")
                    st.text_area("", cv, height=300)
                    st.text(f"Saved as: {filename}")
                    zip_file.write(filename)
            
            # Provide a download button for the ZIP file
            st.markdown("---")
            st.download_button(
                label="📦 Download All CVs as ZIP",
                data=zip_buffer.getvalue(),
                file_name="generated_cvs.zip",
                mime="application/zip"
            )
    else:
        st.error("⚠️ Please enter a job role to generate CVs.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ and Gen-AI by [waqasobeidy@gmail.com](mailto:waqasobeidy@gmail.com)")

# Note:
# - Make sure you set the OPENAI_API_KEY in your environment variables.
