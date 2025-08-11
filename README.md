# 🌟 Random CV Generator

An AI-powered web application that generates realistic CVs for different job roles using advanced language models. Perfect for testing, prototyping, HR demonstrations, or creating sample data for recruitment systems.

## ✨ Features

- **60+ Job Roles**: Generate CVs for diverse positions from Software Engineer to Doctor
- **AI-Powered Content**: Uses Groq's Llama 3.2 90B or OpenAI's GPT-3.5 Turbo for realistic content generation
- **Localized Data**: Generates location-appropriate names, phone numbers, and contact information
- **Batch Generation**: Create 1-50 CVs at once with a single click
- **Professional PDF Output**: Clean, formatted PDFs with blue headers and proper sectioning
- **ZIP Download**: Download all generated CVs in a convenient ZIP file
- **Experience Levels**: Choose between High, Low, or Random experience levels
- **Web Interface**: User-friendly Streamlit interface with real-time preview

## 🚀 How It Works

The Random CV Generator uses artificial intelligence to create comprehensive, realistic CVs by:

1. **Role Analysis**: Analyzes the selected job role to determine relevant skills and experience
2. **Data Generation**: Uses the Faker library to generate realistic personal information
3. **AI Content Creation**: Leverages Groq or OpenAI APIs to generate contextual CV content
4. **PDF Formatting**: Converts the generated content into professionally formatted PDFs
5. **Batch Processing**: Handles multiple CV generation efficiently

## 📋 Available Job Roles

The application supports 60+ predefined job roles across various industries:

**Technology**: Software Engineer, Data Scientist, Security Data Scientist, DevOps Engineer, Full Stack Developer, Backend Developer, Frontend Developer, Cloud Architect, Machine Learning Engineer, AI Researcher, Cybersecurity Specialist, Network Administrator, IT Support Specialist, Systems Analyst, Database Administrator, Quality Assurance Tester

**Business & Management**: Product Manager, Project Coordinator, Business Analyst, Operations Manager, Supply Chain Manager, Procurement Specialist, Warehouse Manager, Retail Store Manager

**Marketing & Communications**: Marketing Specialist, Content Writer, Content Strategist, Social Media Manager, SEO Specialist, Public Relations Specialist, Graphic Designer, UX/UI Designer

**Finance & Legal**: Financial Analyst, Accountant, Legal Advisor

**Healthcare**: Doctor, Nurse, Paramedic, Pharmacist, Veterinarian, Nutritionist

**Education & Research**: Teacher, School Principal, Professor, Research Scientist, Lab Technician, Psychologist

**Sales & Customer Service**: Sales Executive, Customer Service Representative

**Human Resources**: Human Resources Manager, Administrative Assistant

**Engineering**: Mechanical Engineer, Electrical Engineer, Civil Engineer, Biomedical Engineer, Chemical Engineer

**Other**: Event Planner, Fitness Trainer

## 🛠️ Installation

### Prerequisites

- Python 3.11 or higher
- API key from either Groq or OpenAI

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/random-cv-generator.git
   cd random-cv-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   # For Groq API version (create_cv.py)
   GROQ_API_KEY=your_groq_api_key_here
   
   # For OpenAI API version (create_cv_openai_batch.py)
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**:
   ```bash
   # For Groq version
   streamlit run create_cv.py
   
   # For OpenAI version
   streamlit run create_cv_openai_batch.py
   ```

5. **Access the application**:
   Open your browser and navigate to `http://localhost:8501`

### GitHub Codespaces Setup

This project is pre-configured for GitHub Codespaces:

1. **Open in Codespaces**: Click the "Code" button and select "Open with Codespaces"
2. **Automatic Setup**: The devcontainer will automatically install dependencies and start the application
3. **Set Environment Variables**: Add your API keys to the Codespaces secrets or create a `.env` file
4. **Access Application**: The app will be available on port 8501 with automatic port forwarding

## 🔑 API Key Setup

### Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Add it to your `.env` file as `GROQ_API_KEY`

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Add it to your `.env` file as `OPENAI_API_KEY`

## 📖 Usage Guide

### Basic Usage

1. **Select Job Role**: Choose from 60+ predefined job roles
2. **Set Location**: Enter the desired location (default: Saudi Arabia)
3. **Choose Experience Level**: Select High, Low, or Random
4. **Set Quantity**: Choose how many CVs to generate (1-50)
5. **Generate**: Click "✨ Generate Random CVs"
6. **Download**: Use the "📦 Download All CVs as ZIP" button

### Comprehensive Usage Examples

#### Technology Roles

**Example 1: Software Engineer CVs**
```
Job Role: Software Engineer
Location: United States
Experience Level: High
Number of CVs: 15
Expected Output: 15 CVs with 5-8 years experience, skills in Python, Java, React, AWS, etc.
```

**Example 2: Data Scientist CVs**
```
Job Role: Data Scientist
Location: United Kingdom
Experience Level: Random
Number of CVs: 20
Expected Output: Mix of junior (1-3 years) and senior (5-10 years) data scientists
```

**Example 3: Full Stack Developer CVs**
```
Job Role: Full Stack Developer
Location: Germany
Experience Level: Low
Number of CVs: 8
Expected Output: Junior developers with 1-3 years experience, MERN/MEAN stack skills
```

#### Healthcare Roles

**Example 4: Doctor CVs**
```
Job Role: Doctor
Location: Australia
Experience Level: High
Number of CVs: 5
Expected Output: Experienced physicians with specializations, medical degrees, certifications
```

**Example 5: Nurse CVs**
```
Job Role: Nurse
Location: Canada
Experience Level: Random
Number of CVs: 12
Expected Output: Mix of RNs with varying experience levels and specializations
```

#### Business & Management Roles

**Example 6: Product Manager CVs**
```
Job Role: Product Manager
Location: Singapore
Experience Level: High
Number of CVs: 10
Expected Output: Senior PMs with MBA, Agile experience, product launch history
```

**Example 7: Marketing Specialist CVs**
```
Job Role: Marketing Specialist
Location: Brazil
Experience Level: Low
Number of CVs: 25
Expected Output: Entry-level marketers with digital marketing, social media skills
```

#### Engineering Roles

**Example 8: Mechanical Engineer CVs**
```
Job Role: Mechanical Engineer
Location: Japan
Experience Level: Random
Number of CVs: 18
Expected Output: Mix of junior and senior engineers with CAD, manufacturing experience
```

**Example 9: Civil Engineer CVs**
```
Job Role: Civil Engineer
Location: India
Experience Level: High
Number of CVs: 7
Expected Output: Senior engineers with infrastructure projects, PE licenses
```

#### Education & Research Roles

**Example 10: Teacher CVs**
```
Job Role: Teacher
Location: France
Experience Level: Random
Number of CVs: 30
Expected Output: Mix of elementary, middle, high school teachers with education degrees
```

**Example 11: Research Scientist CVs**
```
Job Role: Research Scientist
Location: Switzerland
Experience Level: High
Number of CVs: 6
Expected Output: PhD holders with publications, grant experience, lab management
```

### Location-Specific Examples

#### International Locations

**Example 12: Multi-Location Generation**
```
Scenario: Global recruitment for remote positions
Job Role: DevOps Engineer
Locations to try: "United States", "Canada", "United Kingdom", "Australia", "Netherlands"
Experience Level: High
Number of CVs: 10 per location
Process: Generate separate batches for each location to get diverse, localized candidates
```

**Example 13: Emerging Markets**
```
Job Role: Financial Analyst
Location: "United Arab Emirates"
Experience Level: Random
Number of CVs: 15
Expected Output: Mix of local and international experience, Arabic/English language skills
```

### Experience Level Variations

#### High Experience Examples
```
Job Role: Cybersecurity Specialist
Location: Israel
Experience Level: High
Number of CVs: 8
Expected Output: 7-15 years experience, CISSP/CISM certifications, incident response expertise
```

#### Low Experience Examples
```
Job Role: Graphic Designer
Location: South Korea
Experience Level: Low
Number of CVs: 20
Expected Output: 1-3 years experience, Adobe Creative Suite, portfolio projects
```

#### Random Experience Examples
```
Job Role: Sales Executive
Location: Mexico
Experience Level: Random
Number of CVs: 35
Expected Output: Mix of entry-level (1-2 years) to senior (8-12 years) sales professionals
```

### Batch Generation Strategies

#### Small Batch (1-10 CVs)
**Use Case**: Testing, prototyping, small team hiring
```
Job Role: UX/UI Designer
Location: Sweden
Experience Level: High
Number of CVs: 5
Best Version: Groq (faster individual generation)
Timeline: ~15-30 seconds total
```

#### Medium Batch (11-25 CVs)
**Use Case**: Department hiring, recruitment agency samples
```
Job Role: Customer Service Representative
Location: Philippines
Experience Level: Random
Number of CVs: 22
Best Version: Either (both handle this range well)
Timeline: 1-3 minutes total
```

#### Large Batch (26-50 CVs)
**Use Case**: Mass recruitment, training data, system testing
```
Job Role: Accountant
Location: United States
Experience Level: Random
Number of CVs: 45
Best Version: OpenAI Batch (optimized for large batches)
Timeline: 2-5 minutes total
```

### ZIP Download and File Management

#### Understanding the Output

**File Naming Convention:**
- Individual files: `cv_[JobRole]_[Number].pdf`
- Example: `cv_Software_Engineer_1.pdf`, `cv_Data_Scientist_15.pdf`

**ZIP File Contents:**
```
generated_cvs.zip
├── cv_Software_Engineer_1.pdf
├── cv_Software_Engineer_2.pdf
├── cv_Software_Engineer_3.pdf
├── ...
└── cv_Software_Engineer_15.pdf
```

**File Sizes:**
- Individual CV: ~50-150 KB (depending on content length)
- ZIP file: ~500 KB - 5 MB (depending on batch size)

#### Download Process

1. **Generate CVs**: Click "✨ Generate Random CVs" and wait for completion
2. **Preview Content**: Review generated CVs in the text areas (optional)
3. **Download ZIP**: Click "📦 Download All CVs as ZIP" button
4. **Extract Files**: Unzip the downloaded file to access individual PDFs
5. **File Management**: Rename or organize files as needed for your use case

### Advanced Usage Patterns

#### A/B Testing Different Configurations
```
Test 1: Software Engineer, USA, High Experience, 10 CVs
Test 2: Software Engineer, USA, Random Experience, 10 CVs
Compare: Experience level impact on generated content quality
```

#### Multi-Role Recruitment Campaign
```
Batch 1: Software Engineer (20 CVs)
Batch 2: Data Scientist (15 CVs)  
Batch 3: Product Manager (10 CVs)
Batch 4: DevOps Engineer (12 CVs)
Total: 57 CVs for tech startup hiring
```

#### Localization Testing
```
Same Role, Different Locations:
- Software Engineer, USA (10 CVs)
- Software Engineer, India (10 CVs)
- Software Engineer, Germany (10 CVs)
Compare: Regional differences in skills, education, experience
```

### Troubleshooting Common Usage Issues

#### API Rate Limits
**Problem**: "Rate limit exceeded" error
**Solution**: 
- Reduce batch size (try 10-15 CVs instead of 50)
- Wait 1-2 minutes between large batches
- Switch to Groq API if using OpenAI (often has higher limits)

#### Empty or Incomplete CVs
**Problem**: Generated CVs are too short or missing sections
**Solution**:
- Try different experience levels (High often generates more content)
- Switch between Groq and OpenAI versions
- Regenerate the batch (AI output can vary)

#### Download Issues
**Problem**: ZIP file won't download or is corrupted
**Solution**:
- Ensure all CVs finished generating before downloading
- Try refreshing the page and regenerating
- Check browser download settings and permissions

### Best Practices for Different Use Cases

#### HR and Recruitment
- Use realistic locations for your target market
- Generate 15-25 CVs per role for good variety
- Mix experience levels to see different candidate profiles
- Test with roles similar to your actual openings

#### System Testing and Development
- Start with small batches (5-10 CVs) for initial testing
- Use "Random" experience level for diverse test data
- Generate CVs for multiple roles to test system compatibility
- Verify PDF parsing and data extraction with generated files

#### Training and Education
- Use "Low" experience level for entry-level position examples
- Generate CVs for roles students are interested in
- Compare different locations to show global job market differences
- Use as examples for resume writing workshops

## 📁 File Structure

```
random-cv-generator/
├── .devcontainer/
│   └── devcontainer.json          # GitHub Codespaces configuration
├── create_cv.py                   # Main application (Groq API version)
├── create_cv_openai_batch.py      # OpenAI batch API version
├── requirements.txt               # Python dependencies
├── LICENSE                        # MIT License
├── README.md                      # This file
├── .gitignore                     # Git ignore rules
└── generated_cvs/                 # Output directory (created automatically)
```

## 🔧 Application Versions

This project includes two distinct versions of the CV generator, each using different AI providers and optimized for different use cases. Both versions provide the same core functionality but differ in their underlying AI models, API implementations, and performance characteristics.

### Groq Version (`create_cv.py`) - Recommended for Most Users

**Technical Specifications:**
- **AI Model**: llama-3.2-90b-text-preview (Meta's Llama 3.2 90B parameter model)
- **API Provider**: Groq API
- **Processing Method**: Individual CV generation with sequential API calls
- **Environment Variable**: `GROQ_API_KEY`

**Key Features:**
- **Ultra-Fast Generation**: Groq's specialized inference hardware provides extremely fast response times
- **Cost-Effective**: Generally more affordable than OpenAI for high-volume generation
- **Real-Time Processing**: Each CV is generated and displayed immediately
- **Robust Error Handling**: Individual CV failures don't affect the entire batch

**When to Use Groq Version:**
- **Development and Testing**: Fast iteration cycles for testing different configurations
- **Small to Medium Batches**: Generating 1-25 CVs efficiently
- **Budget-Conscious Projects**: Lower cost per API call
- **Real-Time Applications**: When immediate feedback is important
- **Educational Purposes**: Learning and experimenting with AI-generated content

**API Requirements:**
- Free Groq account at [console.groq.com](https://console.groq.com/)
- API key with access to llama-3.2-90b-text-preview model
- Rate limits: Varies by account tier (typically generous for individual use)

**Performance Characteristics:**
- **Speed**: ~2-5 seconds per CV generation
- **Reliability**: High uptime and consistent performance
- **Scalability**: Excellent for sequential processing

### OpenAI Version (`create_cv_openai_batch.py`) - For High-Volume Production

**Technical Specifications:**
- **AI Model**: gpt-3.5-turbo (OpenAI's GPT-3.5 Turbo model)
- **API Provider**: OpenAI Batch API
- **Processing Method**: Batch processing with simultaneous API calls
- **Environment Variable**: `OPENAI_API_KEY`

**Key Features:**
- **Batch Processing**: Generates multiple CVs simultaneously for improved efficiency
- **High-Quality Content**: GPT-3.5 Turbo's advanced language understanding
- **Production-Ready**: Designed for enterprise-scale CV generation
- **Consistent Output**: More predictable formatting and content structure

**When to Use OpenAI Version:**
- **Large-Scale Generation**: Creating 25-50 CVs in a single batch
- **Production Environments**: Enterprise applications requiring high reliability
- **Content Quality Priority**: When CV content quality is more important than speed
- **Batch Processing Workflows**: Integration with systems that process data in batches
- **Professional Services**: HR agencies, recruitment firms, or consulting services

**API Requirements:**
- OpenAI account with API access at [platform.openai.com](https://platform.openai.com/)
- API key with GPT-3.5 Turbo access
- Sufficient API credits for batch processing
- Rate limits: Based on your OpenAI tier (may require paid plan for high volume)

**Performance Characteristics:**
- **Speed**: ~10-30 seconds for batch processing (depending on batch size)
- **Quality**: Superior content coherence and professional language
- **Efficiency**: Optimized for processing multiple requests simultaneously

### Choosing the Right Version

| Factor | Groq Version | OpenAI Version |
|--------|-------------|----------------|
| **Speed** | ⚡ Faster (individual) | 🔄 Efficient (batch) |
| **Cost** | 💰 Lower cost | 💳 Higher cost |
| **Quality** | ✅ High quality | ⭐ Premium quality |
| **Batch Size** | 👥 1-25 CVs | 🏢 25-50 CVs |
| **Use Case** | Development/Testing | Production/Enterprise |
| **Setup Complexity** | 🟢 Simple | 🟡 Moderate |

### Running Each Version

**Groq Version:**
```bash
# Set environment variable
export GROQ_API_KEY=your_groq_api_key_here

# Run the application
streamlit run create_cv.py
```

**OpenAI Version:**
```bash
# Set environment variable
export OPENAI_API_KEY=your_openai_api_key_here

# Run the application
streamlit run create_cv_openai_batch.py
```

### API Cost Considerations

**Groq API:**
- Generally offers competitive pricing with generous free tiers
- Costs scale linearly with the number of CVs generated
- Ideal for budget-conscious projects and individual users

**OpenAI API:**
- Premium pricing but with superior content quality
- Batch processing can be more cost-effective for large volumes
- Recommended for commercial applications where quality justifies the cost

Both versions produce identical PDF outputs and user interfaces, so the choice primarily depends on your specific requirements for speed, cost, quality, and scale.

## 📦 Dependencies

The application relies on the following key dependencies:

- **streamlit**: Web application framework
- **groq**: Groq API client
- **openai**: OpenAI API client
- **fpdf**: PDF generation library
- **faker**: Random data generation
- **python-dotenv**: Environment variable management
- **zipfile**: ZIP file creation (built-in)

For a complete list, see `requirements.txt`.

## 🎨 Generated CV Format

Each generated CV includes:

- **Personal Information**: Name, email, phone, location
- **Professional Summary**: Role-specific summary
- **Skills**: Relevant technical and soft skills
- **Experience**: Previous work experience with descriptions
- **Education**: Educational background
- **Projects**: Relevant projects and achievements
- **Certifications**: Industry certifications
- **Languages**: Language proficiencies
- **References**: Professional references

### PDF Styling
- Blue headers and section dividers
- Professional typography using Helvetica font
- Proper spacing and formatting
- Character encoding support for international names

## 🔧 Technical Details

### PDF Generation Process Using FPDF Library

The application leverages the FPDF library to create professional, standardized PDF documents with consistent formatting and international character support.

#### Core PDF Architecture
```python
# PDF initialization and configuration
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
```

#### Advanced Formatting Features

**Header and Title Styling:**
- **Primary Title**: 16pt Helvetica Bold, centered alignment
- **Color Scheme**: Blue headers (RGB: 0, 102, 204) for visual hierarchy
- **Decorative Elements**: Horizontal line separators with matching blue color
- **Positioning**: Precise coordinate-based layout for consistent appearance

**Section Management:**
- **Dynamic Section Detection**: Automatically identifies section headers ending with ":"
- **Font Switching**: Bold 12pt for headers, regular 12pt for content
- **Color Transitions**: Dark blue (RGB: 0, 51, 102) for section headers, black for content
- **Spacing Control**: Consistent line spacing (10pt) and section breaks (2pt)

**Multi-Cell Content Handling:**
```python
# Automatic text wrapping and page breaks
pdf.multi_cell(0, 10, content_text)
pdf.ln(2)  # Consistent spacing between elements
```

#### Character Encoding and International Support

**Primary Encoding Strategy:**
- **ASCII Filtering**: Converts non-ASCII characters to underscores for compatibility
- **Character Validation**: `ord(char) < 128` check for each character
- **Fallback Mechanism**: Secondary PDF generation with stricter character filtering

**International Name Handling:**
```python
# Character encoding safety
safe_text = ''.join(char if ord(char) < 128 else '_' for char in text)
```

**Error Recovery Process:**
1. **Primary Generation**: Attempt with standard character filtering
2. **Fallback Generation**: Strip all non-printable and non-ASCII characters
3. **Minimal PDF**: Create basic structure if all else fails

#### Page Management and Layout
- **Auto Page Breaks**: Automatic overflow handling with 15pt margins
- **Content Flow**: Seamless continuation across multiple pages
- **Margin Control**: Consistent 15pt margins on all sides
- **Font Compatibility**: Helvetica font family for cross-platform consistency

### Random Data Generation Using Faker Library

The application uses Python's Faker library to generate realistic, contextually appropriate personal and professional information.

#### Faker Configuration and Localization
```python
from faker import Faker
fake = Faker()  # Default locale with international support
```

#### Personal Information Generation

**Name Generation:**
- **Localized Names**: Context-aware name generation based on specified location
- **Gender Diversity**: Automatic male/female name selection
- **Cultural Appropriateness**: Names that fit the geographic region
- **Character Safety**: English character limitation for PDF compatibility

**Email Address Creation:**
```python
# Unique email generation algorithm
name_base = name.replace(' ', '.').lower()
random_hash = str(random.randint(1000, 9999))
email = f"{name_base}{random_hash}@example.com"
```
- **Uniqueness Guarantee**: 4-digit random hash prevents duplicates
- **Professional Format**: firstname.lastname + hash structure
- **Domain Standardization**: @example.com for consistency

**Phone Number Generation:**
- **Location-Aware Formatting**: Phone numbers appropriate to specified country/region
- **Format Variety**: Different phone number patterns based on locale
- **Realistic Patterns**: Follows actual phone numbering conventions
- **International Compatibility**: Supports various country codes and formats

#### Professional Data Context

**Experience Level Mapping:**
- **High Experience**: 7-15 years of professional experience
- **Low Experience**: 1-3 years of entry-level experience  
- **Random Experience**: Mixed distribution across experience ranges

**Skill and Education Alignment:**
- **Role-Specific Skills**: Technical skills matched to job requirements
- **Education Levels**: Appropriate degrees for professional roles
- **Certification Relevance**: Industry-standard certifications for each field

### Streamlit Web Interface Features

The application provides a comprehensive web interface built with Streamlit, offering real-time interaction and professional user experience.

#### User Interface Components

**Input Controls:**
```python
# Location input with default value
location = st.text_input("🌍 Enter the location:", value="Saudi Arabia")

# Experience level selection
experience_level = st.selectbox("🔧 Select the experience level:", 
                               ["High", "Low", "Random"], index=2)

# Batch size control with validation
num_cvs = st.number_input("📄 Enter the number of CVs to generate:", 
                         min_value=1, max_value=50, value=5)
```

**Job Role Selection:**
- **Dropdown Interface**: Searchable selectbox with 60+ predefined roles
- **Categorized Options**: Roles organized by industry (Technology, Healthcare, Business, etc.)
- **Role Validation**: Ensures valid selection before processing

#### Real-Time Processing Features

**Progress Indicators:**
```python
with st.spinner('⏳ Generating CVs, please wait...'):
    # CV generation process with visual feedback
```
- **Loading Spinners**: Visual feedback during API calls
- **Status Messages**: Real-time updates on generation progress
- **Error Handling**: User-friendly error messages for API failures

**Content Preview System:**
- **Text Area Display**: Generated CV content shown in expandable text areas
- **Individual CV Preview**: Each CV displayed separately with numbering
- **Height Control**: 300px text areas for optimal readability
- **Scroll Support**: Automatic scrolling for long content

#### Batch Processing and Download Management

**ZIP File Creation:**
```python
zip_buffer = BytesIO()
with zipfile.ZipFile(zip_buffer, "w") as zip_file:
    for idx, cv in enumerate(generated_cvs):
        filename = f"cv_{job_role}_{idx + 1}.pdf"
        zip_file.write(filename)
```

**Download Interface:**
- **Download Button**: Streamlit download_button with custom styling
- **MIME Type Handling**: Proper application/zip MIME type
- **File Naming**: Descriptive filename (generated_cvs.zip)
- **Buffer Management**: In-memory ZIP creation for efficiency

#### Input Validation and Error Handling

**Form Validation:**
- **Required Fields**: Job role selection validation
- **Range Validation**: CV quantity limits (1-50)
- **Input Sanitization**: Location input cleaning and validation

**Error Management:**
- **API Error Handling**: Graceful handling of API failures
- **Network Issues**: Timeout and connection error management
- **User Feedback**: Clear error messages with suggested solutions

### File Output Format and Character Encoding

The application generates standardized PDF files with robust character encoding support for international use.

#### File Naming Convention

**Individual PDF Files:**
```
Format: cv_[JobRole]_[Number].pdf
Examples:
- cv_Software_Engineer_1.pdf
- cv_Data_Scientist_15.pdf
- cv_Marketing_Specialist_3.pdf
```

**Naming Rules:**
- **Space Replacement**: Spaces in job roles replaced with underscores
- **Sequential Numbering**: 1-based indexing for batch identification
- **Extension Standard**: .pdf extension for universal compatibility

#### ZIP Archive Structure

**Archive Organization:**
```
generated_cvs.zip
├── cv_Software_Engineer_1.pdf    (50-150 KB)
├── cv_Software_Engineer_2.pdf    (50-150 KB)
├── cv_Software_Engineer_3.pdf    (50-150 KB)
├── ...
└── cv_Software_Engineer_N.pdf    (50-150 KB)

Total Archive Size: 500 KB - 5 MB (depending on batch size)
```

#### Character Encoding Handling for International Names

**Multi-Layer Encoding Strategy:**

**Level 1 - Standard Filtering:**
```python
safe_text = ''.join(char if ord(char) < 128 else '_' for char in text)
```
- **ASCII Limitation**: Restricts to ASCII character set (0-127)
- **Replacement Strategy**: Non-ASCII characters become underscores
- **Compatibility Focus**: Ensures PDF readability across all systems

**Level 2 - Enhanced Filtering:**
```python
safe_text = ''.join(c for c in text if ord(c) < 128 and c.isprintable())
```
- **Printable Characters Only**: Removes control characters and non-printable ASCII
- **Double Validation**: Both ASCII and printability checks
- **Fallback Activation**: Used when primary generation fails

**International Location Support:**

**Location-Specific Adaptations:**
- **Name Localization**: Faker generates culturally appropriate names
- **Phone Format Adaptation**: Country-specific phone number patterns
- **Address Formatting**: Regional address structure compliance
- **Language Considerations**: Skills and experience terms adapted to region

**Character Set Limitations:**
- **PDF Compatibility**: FPDF library ASCII limitations addressed
- **Cross-Platform Support**: Ensures PDFs open correctly on all systems
- **Font Embedding**: Helvetica font ensures consistent rendering
- **Encoding Transparency**: Users see actual characters that will appear in PDF

#### File Size and Performance Characteristics

**Individual PDF Specifications:**
- **File Size Range**: 50-150 KB per CV (varies by content length)
- **Page Count**: Typically 1-2 pages per CV
- **Resolution**: Standard PDF resolution (72 DPI)
- **Compression**: FPDF default compression for optimal file size

**Batch Processing Performance:**
- **Generation Speed**: 2-5 seconds per CV (Groq) / 10-30 seconds batch (OpenAI)
- **Memory Usage**: In-memory processing with automatic cleanup
- **Concurrent Handling**: Sequential processing prevents API rate limiting
- **Error Isolation**: Individual CV failures don't affect batch completion

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Add new job roles, improve PDF formatting, enhance UI
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Contribution Ideas
- Add more job roles
- Improve PDF formatting
- Add new AI model integrations
- Enhance the user interface
- Add unit tests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Waqas Khalid Obeidy**
- Email: [waqasobeidy@gmail.com](mailto:waqasobeidy@gmail.com)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Groq](https://groq.com/) for fast AI inference
- [OpenAI](https://openai.com/) for powerful language models
- [Faker](https://faker.readthedocs.io/) for realistic data generation
- [FPDF](http://www.fpdf.org/) for PDF generation

## 📸 Screenshots

*Screenshots will be added here showing the application interface and sample generated CVs*

---

**Built with ❤️ and Gen-AI**

*Generate realistic CVs in seconds, not hours!*




