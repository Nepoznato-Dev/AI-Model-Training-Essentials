# Document Formatting & Conversion

Master the art of converting and formatting content across multiple file formats for different platforms, tools, and use cases.

## Overview

Document formatting is the essential skill of transforming content from one format to another while preserving meaning, structure, and readability. This skill enables you to adapt your work for various stakeholders, systems, and distribution channels. Whether you need to share a simple text file, create a professional Word document, export data to CSV, or structure content as JSON/XML, this guide provides the frameworks and techniques to do it effectively.

## Core Competencies

- **Format Recognition**: Understanding the purpose and characteristics of different file formats
- **Structure Preservation**: Maintaining content hierarchy and relationships during conversion
- **Platform Compatibility**: Ensuring files work across different operating systems and applications
- **Data Integrity**: Preserving all information without loss during transformation
- **Audience Adaptation**: Choosing the right format for the intended use case

## Format Categories

### Text-Based Formats

#### 1. Plain Text (.txt)
**Purpose**: Universal, lightweight, maximum compatibility

**Characteristics**:
- No formatting (bold, italics, etc.)
- No images or multimedia
- ASCII or Unicode encoding
- Smallest file size
- Opens in any text editor

**Best For**:
- Simple notes and documentation
- Code snippets
- Log files
- Configuration files
- Maximum portability

**Conversion Guidelines**:
```
Markdown → TXT:
- Remove all markdown syntax (#, *, _, `, etc.)
- Convert links to plain URLs: [Text](url) → url
- Convert headers to uppercase or add spacing
- Replace tables with simple text layouts
- Remove image references or describe them in text
```

**Example**:
```markdown
# Original Markdown
## Features
- **Fast** processing
- [Learn more](https://example.com)
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
```

```txt
Converted to Plain Text:
FEATURES

* Fast processing
* Learn more: https://example.com

Column 1    Column 2
Data 1      Data 2
```

---

#### 2. Rich Text Format (.rtf)
**Purpose**: Cross-platform formatted text with basic styling

**Characteristics**:
- Supports bold, italic, underline
- Font changes and sizes
- Basic colors
- Simple tables
- Widely supported

**Best For**:
- Formatted documents for email
- Documents needing basic styling
- Cross-platform sharing
- Legacy system compatibility

**RTF Structure Template**:
```rtf
{\rtf1\ansi\deff0
{\fonttbl
{\f0\fswiss\fprq2\fcharset0 Arial;}
{\f1\froman\fprq2\fcharset0 Times New Roman;}
}
{\colortbl;\red0\green0\blue0;\red255\green0\blue0;}
\f0\fs24\b Header Text\b0\par
\i Italic Text\i0\par
{\pard\ql Regular paragraph\par}
{\pard\qc Centered text\par}
}
```

**Common RTF Commands**:
- `\b` / `\b0` - Bold on/off
- `\i` / `\i0` - Italic on/off
- `\ul` / `\ul0` - Underline on/off
- `\par` - Paragraph break
- `\qc` - Center alignment
- `\qr` - Right alignment
- `\ql` - Left alignment (default)
- `\fsNN` - Font size (NN = half-points, so \fs24 = 12pt)

---

#### 3. Microsoft Word (.doc, .docx)
**Purpose**: Professional documents with advanced formatting

**Characteristics**:
- .doc: Binary format (Word 97-2003)
- .docx: XML-based ZIP archive (Word 2007+)
- Full formatting support
- Images, charts, tables
- Track changes and comments
- Macros support (.docm)

**Best For**:
- Business reports
- Resumes and CVs
- Formal documents
- Collaborative editing
- Print-ready materials

**Markdown to Word Conversion Strategy**:

```python
# Using pandoc (recommended tool)
# Command line:
pandoc input.md -o output.docx

# With custom reference document:
pandoc input.md --reference-doc=template.docx -o output.docx

# Python alternative using python-docx
from docx import Document

doc = Document()
doc.add_heading('Document Title', 0)
doc.add_paragraph('Bold text', style='Intense Quote')
doc.save('output.docx')
```

**Word Format Best Practices**:
1. Use Styles consistently (Heading 1, Heading 2, etc.)
2. Embed fonts for portability
3. Compress images to reduce file size
4. Use built-in table features, not manual spacing
5. Add alt text to images for accessibility
6. Use section breaks for complex layouts

---

#### 4. Apple Pages (.pages)
**Purpose**: macOS/iOS native document format

**Characteristics**:
- ZIP archive containing XML and assets
- Modern, clean design templates
- iCloud integration
- Real-time collaboration
- Export to multiple formats

**Best For**:
- Apple ecosystem users
- Visually appealing documents
- Quick flyers and posters
- Collaborative projects on Mac/iPad

**Conversion Notes**:
```bash
# Pages files are ZIP archives
# To inspect contents:
unzip document.pages -d extracted_pages/

# Contains:
# - Index.xml (main content)
# - Metadata.plist
# - Preview.pdf
# - Data/ folder (images, etc.)

# Convert to Word format:
# In Pages app: File → Export To → Word
# Or use cloud conversion services
```

---

### Data Formats

#### 5. Comma-Separated Values (.csv)
**Purpose**: Tabular data exchange between applications

**Characteristics**:
- Plain text format
- Rows separated by newlines
- Columns separated by commas (or other delimiters)
- Optional header row
- Universal spreadsheet support

**Best For**:
- Database exports/imports
- Spreadsheet data exchange
- Data analysis workflows
- Simple data storage

**CSV Structure**:
```csv
name,email,age,department
"John Doe",john@example.com,30,Engineering
"Jane Smith",jane@example.com,28,Marketing
"Bob Johnson",bob@example.com,35,Sales
```

**Markdown Table to CSV**:
```markdown
| Name | Email | Age |
|------|-------|-----|
| John | john@example.com | 30 |
| Jane | jane@example.com | 28 |
```

```csv
Name,Email,Age
John,john@example.com,30
Jane,jane@example.com,28
```

**CSV Best Practices**:
1. Always include a header row
2. Quote fields containing commas, quotes, or newlines
3. Escape quotes by doubling them: `"He said ""Hello"""`
4. Use UTF-8 encoding for international characters
5. Be consistent with line endings (LF vs CRLF)
6. Avoid trailing commas

**Common Issues & Solutions**:
```python
import csv

# Reading CSV properly
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'])

# Writing CSV properly
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Name', 'Email', 'Age'])
    writer.writerow(['John', 'john@example.com', 30])
```

---

#### 6. JavaScript Object Notation (.json)
**Purpose**: Structured data interchange, especially for web APIs

**Characteristics**:
- Key-value pairs
- Hierarchical structure
- Human-readable
- Machine-parseable
- Language-independent

**Best For**:
- API responses
- Configuration files
- Data serialization
- NoSQL databases

**JSON Structure**:
```json
{
  "skill": "Document Formatting",
  "version": 1.0,
  "formats": [
    {
      "extension": ".txt",
      "name": "Plain Text",
      "features": ["universal", "lightweight"]
    },
    {
      "extension": ".json",
      "name": "JSON",
      "features": ["structured", "hierarchical"]
    }
  ],
  "metadata": {
    "author": "Skills Repository",
    "created": "2026-01-15",
    "tags": ["formatting", "conversion", "documentation"]
  }
}
```

**JSON Rules**:
1. Use double quotes for strings (no single quotes)
2. Keys must be quoted strings
3. No trailing commas
4. Valid values: string, number, object, array, true, false, null
5. No comments (use separate documentation if needed)

**Markdown to JSON Conversion**:
```python
import json
import re

def markdown_to_json(md_content):
    """Convert structured markdown to JSON"""
    data = {
        "title": "",
        "sections": [],
        "metadata": {}
    }
    
    # Extract title (first h1)
    title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    if title_match:
        data["title"] = title_match.group(1)
    
    # Extract sections (h2 headers)
    sections = re.split(r'^##\s+', md_content, flags=re.MULTILINE)
    for section in sections[1:]:  # Skip title section
        lines = section.strip().split('\n')
        section_title = lines[0]
        section_content = '\n'.join(lines[1:])
        data["sections"].append({
            "title": section_title,
            "content": section_content
        })
    
    return json.dumps(data, indent=2)
```

**JSON Validation**:
```bash
# Using jq (command-line JSON processor)
jq '.' input.json  # Pretty print and validate

# Using Python
python -m json.tool input.json

# Online validators: jsonlint.com, jsonformatter.org
```

---

#### 7. Extensible Markup Language (.xml)
**Purpose**: Structured data with schema validation, document markup

**Characteristics**:
- Tag-based structure
- Self-describing
- Schema validation (XSD, DTD)
- Namespace support
- Verbose but explicit

**Best For**:
- Configuration files
- Document formats (DOCX, XLSX are XML-based)
- SOAP APIs
- RSS/Atom feeds
- Vector graphics (SVG)

**XML Structure**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<skills>
    <skill name="Document Formatting" version="1.0">
        <description>
            Master the art of converting and formatting content
        </description>
        <formats>
            <format extension=".txt">
                <name>Plain Text</name>
                <features>
                    <feature>universal</feature>
                    <feature>lightweight</feature>
                </features>
            </format>
            <format extension=".json">
                <name>JSON</name>
                <features>
                    <feature>structured</feature>
                    <feature>hierarchical</feature>
                </features>
            </format>
        </formats>
        <metadata>
            <author>Skills Repository</author>
            <created>2026-01-15</created>
            <tags>
                <tag>formatting</tag>
                <tag>conversion</tag>
            </tags>
        </metadata>
    </skill>
</skills>
```

**XML Best Practices**:
1. Always include XML declaration
2. Use meaningful tag names
3. Close all tags properly
4. Escape special characters: `&lt;`, `&gt;`, `&amp;`, `&quot;`, `&apos;`
5. Use attributes sparingly (prefer child elements for data)
6. Validate against schema when possible

**XML Validation**:
```bash
# Using xmllint
xmllint --noout --schema schema.xsd document.xml

# Using Python
from xml.etree import ElementTree
try:
    tree = ElementTree.parse('document.xml')
    print("Valid XML")
except ElementTree.ParseError as e:
    print(f"Invalid XML: {e}")
```

---

#### 8. Structured Data Format (.sdf)
**Purpose**: Various specialized structured data formats

**Note**: SDF can refer to multiple formats:
- **Chemical SDF**: Structure-data format for molecular data
- **Simple Data Format**: Generic tabular data format
- **System Data Format**: Platform-specific system data

**Chemical SDF Example** (most common):
```sdf
Molecule_Name_001
  -OEChem-         

 22 24  0     0  0  0  0  0  0999 V2000
    1.2345   2.3456   0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.3456   3.4567   0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
M  END
>  <FORMULA>
C6H12O6

>  <MOLECULAR_WEIGHT>
180.16

>  <SOURCE>
Skills Repository

$$$$
```

**Generic SDF Template**:
```sdf
RECORD_ID: 001
FIELD_NAME: Value
ANOTHER_FIELD: Another Value
MULTI_LINE: Line 1
  Line 2
  Line 3
//
RECORD_ID: 002
FIELD_NAME: Different Value
//
```

---

#### 9. Excel Spreadsheet (.xlsx)
**Purpose**: Complex spreadsheets with formulas, charts, and formatting

**Characteristics**:
- ZIP archive of XML files
- Multiple worksheets
- Formulas and functions
- Charts and graphs
- Conditional formatting
- Pivot tables

**Best For**:
- Financial models
- Data analysis
- Reports with calculations
- Dashboards
- Complex data visualization

**XLSX Structure** (internal):
```
workbook.xlsx (ZIP archive containing):
├── _rels/
│   └── .rels
├── xl/
│   ├── _rels/
│   │   └── workbook.xml.rels
│   ├── worksheets/
│   │   ├── sheet1.xml
│   │   └── sheet2.xml
│   ├── workbook.xml
│   ├── styles.xml
│   └── sharedStrings.xml
└── [Content_Types].xml
```

**Creating XLSX from Markdown**:
```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Skills Data"

# Add headers with formatting
headers = ["Skill", "Category", "Level", "Status"]
for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = Font(bold=True)
    cell.fill = PatternFill(start_color="DDDDDD", end_color="DDDDDD", fill_type="solid")
    cell.alignment = Alignment(horizontal="center")

# Add data
data = [
    ["Document Formatting", "Communication", "Advanced", "Complete"],
    ["Markdown", "Writing", "Expert", "Complete"],
    ["Data Conversion", "Technical", "Intermediate", "In Progress"]
]

for row_idx, row_data in enumerate(data, 2):
    for col_idx, value in enumerate(row_data, 1):
        ws.cell(row=row_idx, column=col_idx, value=value)

# Auto-adjust column widths
for column in ws.columns:
    max_length = 0
    column_letter = column[0].column_letter
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = min(max_length + 2, 50)
    ws.column_dimensions[column_letter].width = adjusted_width

# Save
wb.save('skills_data.xlsx')
```

**CSV to XLSX Conversion**:
```python
import pandas as pd

# Read CSV
df = pd.read_csv('input.csv')

# Write to Excel with formatting
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
    
    # Access the workbook and worksheet
    workbook = writer.book
    worksheet = writer.sheets['Data']
    
    # Add formatting as needed
```

---

## Conversion Framework

### The FORMAT Method

A systematic approach to format conversion:

**F** - **Final Format Identification**
- Determine the target format based on use case
- Consider audience and platform requirements
- Identify any format constraints

**O** - **Original Content Analysis**
- Assess source format capabilities
- Identify elements that may not translate
- Plan workarounds for incompatible features

**R** - **Relationship Mapping**
- Map source elements to target equivalents
- Preserve hierarchical relationships
- Maintain data integrity

**M** - **Metadata Handling**
- Transfer or adapt metadata appropriately
- Update timestamps and version info
- Preserve authorship information

**A** - **Adaptation & Transformation**
- Execute the conversion
- Handle edge cases and special characters
- Apply format-specific optimizations

**T** - **Testing & Validation**
- Verify content completeness
- Test file opening in target applications
- Validate against format specifications

**Example Application**:

Converting a Markdown skill document to multiple formats:

```markdown
# Source: skill.md
## Section 1
Content here with **bold** and *italic*
- List item 1
- List item 2
```

**Step 1: Identify Target Formats**
- .txt for universal access
- .docx for professional sharing
- .pdf for distribution
- .html for web publishing

**Step 2: Analyze Content**
- Headers need adaptation per format
- Bold/italic supported in most formats
- Lists convert well universally

**Step 3: Execute Conversions**
```bash
# To TXT
pandoc skill.md -o skill.txt

# To DOCX
pandoc skill.md -o skill.docx

# To PDF (via LaTeX or HTML)
pandoc skill.md -o skill.pdf

# To HTML
pandoc skill.md -o skill.html
```

**Step 4: Validate Outputs**
- Check each file opens correctly
- Verify formatting preserved appropriately
- Ensure no content loss

---

## Practical Templates

### Template 1: Multi-Format Export Script

```python
#!/usr/bin/env python3
"""
Multi-format document exporter
Converts Markdown to various formats
"""

import os
import subprocess
import json
from pathlib import Path

class DocumentExporter:
    def __init__(self, source_file):
        self.source = Path(source_file)
        self.output_dir = self.source.parent / 'exports'
        self.output_dir.mkdir(exist_ok=True)
    
    def export_all(self):
        """Export to all supported formats"""
        formats = {
            'txt': self.to_txt,
            'docx': self.to_docx,
            'pdf': self.to_pdf,
            'html': self.to_html,
            'json': self.to_json,
            'xml': self.to_xml,
        }
        
        results = {}
        for fmt, method in formats.items():
            try:
                output_path = method()
                results[fmt] = {'status': 'success', 'path': str(output_path)}
            except Exception as e:
                results[fmt] = {'status': 'failed', 'error': str(e)}
        
        return results
    
    def to_txt(self):
        output = self.output_dir / f"{self.source.stem}.txt"
        subprocess.run(['pandoc', str(self.source), '-o', str(output)], check=True)
        return output
    
    def to_docx(self):
        output = self.output_dir / f"{self.source.stem}.docx"
        subprocess.run(['pandoc', str(self.source), '-o', str(output)], check=True)
        return output
    
    def to_pdf(self):
        output = self.output_dir / f"{self.source.stem}.pdf"
        subprocess.run(['pandoc', str(self.source), '-o', str(output)], check=True)
        return output
    
    def to_html(self):
        output = self.output_dir / f"{self.source.stem}.html"
        subprocess.run(['pandoc', str(self.source), '-o', str(output)], check=True)
        return output
    
    def to_json(self):
        output = self.output_dir / f"{self.source.stem}.json"
        # Custom conversion logic
        content = self.source.read_text()
        json_data = {
            'title': self.source.stem,
            'content': content,
            'format': 'markdown'
        }
        output.write_text(json.dumps(json_data, indent=2))
        return output
    
    def to_xml(self):
        output = self.output_dir / f"{self.source.stem}.xml"
        # Custom conversion logic
        content = self.source.read_text()
        xml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
<document>
    <metadata>
        <title>{self.source.stem}</title>
        <source>{self.source.name}</source>
    </metadata>
    <content>
        {self._escape_xml(content)}
    </content>
</document>"""
        output.write_text(xml_data)
        return output
    
    def _escape_xml(self, text):
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;'))

# Usage
if __name__ == '__main__':
    exporter = DocumentExporter('my_document.md')
    results = exporter.export_all()
    print(json.dumps(results, indent=2))
```

### Template 2: Format Selection Decision Tree

```
What is your primary goal?
│
├─ Maximum Compatibility
│  └─→ Use .txt or .pdf
│
├─ Editable Document
│  ├─ Microsoft Office users → .docx
│  ├─ Apple users → .pages
│  └─ Cross-platform → .rtf or .docx
│
├─ Data Exchange
│  ├─ Tabular data → .csv or .xlsx
│  ├─ API/Web → .json
│  ├─ Enterprise systems → .xml
│  └─ Scientific data → .sdf
│
├─ Web Publishing
│  └─→ .html or .md
│
├─ Print Publication
│  └─→ .pdf or .docx
│
└─ Version Control
   └─→ .md or .txt (not binary formats)
```

---

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Losing formatting during conversion | Unprofessional appearance | Choose appropriate target format; use proper conversion tools |
| Character encoding issues | Garbled text, lost special characters | Always specify UTF-8 encoding; test with international characters |
| Breaking hyperlinks | Non-functional references | Verify links after conversion; use absolute paths when needed |
| Image loss or corruption | Missing visual content | Embed images properly; use base64 for some formats; keep original assets |
| Table misalignment | Data becomes unreadable | Use format-appropriate table structures; test with sample data |
| Metadata loss | Lost authorship, dates, versions | Explicitly transfer metadata; use format-specific metadata fields |
| File size explosion | Slow transfers, storage issues | Compress images; remove unnecessary elements; choose efficient formats |
| Incompatible features | Elements don't render | Know format limitations; provide fallbacks; simplify complex content |

---

## Best Practices

1. **Always Keep Original Source Files**
   - Maintain the master copy in the most flexible format
   - Use version control for text-based formats
   - Never edit converted files; always regenerate from source

2. **Test Across Platforms**
   - Open files in multiple applications
   - Test on different operating systems
   - Verify mobile compatibility when relevant

3. **Document Your Conversion Process**
   - Record which tools and versions were used
   - Note any manual adjustments required
   - Create reproducible scripts for automation

4. **Validate Output Quality**
   - Compare content before and after conversion
   - Check for missing elements
   - Verify formatting meets requirements

5. **Consider Accessibility**
   - Add alt text to images
   - Use proper heading hierarchy
   - Ensure sufficient color contrast
   - Make tables accessible with proper headers

6. **Optimize for Purpose**
   - Don't over-format simple content
   - Choose the simplest format that meets needs
   - Balance features with compatibility

7. **Batch Process When Possible**
   - Automate repetitive conversions
   - Use scripts for consistency
   - Implement quality checks in automation

---

## Tools & Resources

### Conversion Tools

- **Pandoc** (pandoc.org) - Universal document converter
  ```bash
  pandoc input.md -o output.docx
  pandoc input.md -o output.pdf
  pandoc input.md -o output.html
  ```

- **LibreOffice** - Free office suite with CLI conversion
  ```bash
  libreoffice --headless --convert-to pdf document.docx
  libreoffice --headless --convert-to txt document.odt
  ```

- **Calibre** - E-book format conversion
  ```bash
  ebook-convert input.epub output.mobi
  ```

- **Online Converters**:
  - CloudConvert (cloudconvert.com)
  - Zamzar (zamzar.com)
  - ILovePDF (ilovepdf.com)

### Programming Libraries

**Python**:
- `python-docx` - Create/edit Word documents
- `openpyxl` - Work with Excel files
- `reportlab` - Generate PDFs
- `json` (built-in) - JSON handling
- `xml.etree.ElementTree` (built-in) - XML parsing
- `csv` (built-in) - CSV operations

**JavaScript/Node.js**:
- `docx` - Word document generation
- `exceljs` - Excel file manipulation
- `pdfkit` - PDF creation
- `fast-xml-parser` - XML handling

**Command Line**:
- `jq` - JSON processing
- `xmllint` - XML validation
- `csvkit` - CSV utilities
- `pdftk` - PDF manipulation

### Validators

- **JSON**: jsonlint.com, JSONLint browser extension
- **XML**: xmlvalidation.com, W3C Markup Validator
- **CSV**: csvlint.io, Beanstalk CSV Validator
- **Accessibility**: WAVE (wave.webaim.org), axe DevTools

---

## Example Applications

### Scenario 1: Technical Documentation Distribution

**Challenge**: Share technical documentation with diverse stakeholders using different tools.

**Solution**:
```bash
# Source: docs.md (Markdown)

# Generate all required formats
pandoc docs.md -o docs.txt          # For developers (quick viewing)
pandoc docs.md -o docs.docx         # For management (Word users)
pandoc docs.md -o docs.pdf          # For external distribution
pandoc docs.md -o docs.html         # For intranet posting
pandoc docs.md -o docs.json         # For API documentation

# Create README with format descriptions
cat > README.md << EOF
# Documentation Package

Available formats:
- docs.txt: Plain text, opens everywhere
- docs.docx: Microsoft Word, editable
- docs.pdf: Fixed layout, print-ready
- docs.html: Web browser viewing
- docs.json: Machine-readable format
EOF
```

### Scenario 2: Data Migration Project

**Challenge**: Migrate data from legacy CSV system to modern JSON API.

**Solution**:
```python
import csv
import json
from datetime import datetime

def migrate_csv_to_json(csv_path, json_path):
    """Migrate CSV data to JSON with validation"""
    
    records = []
    errors = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row_num, row in enumerate(reader, 2):
            try:
                # Transform and validate
                record = {
                    'id': int(row['id']),
                    'name': row['name'].strip(),
                    'email': row['email'].lower().strip(),
                    'created_at': datetime.fromisoformat(row['created']),
                    'metadata': {
                        'source': 'legacy_csv',
                        'migration_date': datetime.now().isoformat(),
                        'original_row': row_num
                    }
                }
                
                # Validate email format
                if '@' not in record['email']:
                    raise ValueError(f"Invalid email: {record['email']}")
                
                records.append(record)
                
            except Exception as e:
                errors.append({
                    'row': row_num,
                    'error': str(e),
                    'data': dict(row)
                })
    
    # Write successful records
    output = {
        'version': '1.0',
        'migrated_at': datetime.now().isoformat(),
        'total_records': len(records),
        'errors_count': len(errors),
        'data': records
    }
    
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(output, jsonfile, indent=2, default=str)
    
    # Log errors
    if errors:
        with open('migration_errors.json', 'w') as errfile:
            json.dump(errors, errfile, indent=2)
    
    return len(records), len(errors)

# Usage
success, failed = migrate_csv_to_json('users.csv', 'users.json')
print(f"Migrated {success} records, {failed} errors")
```

### Scenario 3: Report Generation Pipeline

**Challenge**: Generate monthly reports in multiple formats for different departments.

**Solution**:
```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
from datetime import datetime

def generate_monthly_report(data_df, month, year):
    """Generate report in PDF, XLSX, and HTML"""
    
    timestamp = f"{year}_{month:02d}"
    
    # 1. PDF Report
    pdf_path = f"reports/monthly_report_{timestamp}.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph(f"Monthly Report - {month}/{year}", styles['Title']))
    story.append(Spacer(1, 20))
    
    # Summary
    story.append(Paragraph("Executive Summary", styles['Heading2']))
    story.append(Paragraph(f"Total Records: {len(data_df)}", styles['Normal']))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Data Table
    story.append(Paragraph("Data Overview", styles['Heading2']))
    table_data = [list(data_df.columns)] + data_df.values.tolist()
    table = Table(table_data)
    story.append(table)
    
    doc.build(story)
    
    # 2. Excel Report
    xlsx_path = f"reports/monthly_report_{timestamp}.xlsx"
    with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
        data_df.to_excel(writer, sheet_name='Data', index=False)
        
        # Add summary sheet
        summary_df = pd.DataFrame({
            'Metric': ['Total Records', 'Generation Date'],
            'Value': [len(data_df), datetime.now().isoformat()]
        })
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    # 3. HTML Report
    html_path = f"reports/monthly_report_{timestamp}.html"
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Monthly Report {month}/{year}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #2c3e50; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #3498db; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Monthly Report - {month}/{year}</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        <h2>Data Overview</h2>
        {data_df.to_html(index=False)}
    </body>
    </html>
    """
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return {
        'pdf': pdf_path,
        'excel': xlsx_path,
        'html': html_path
    }

# Usage
df = pd.read_csv('monthly_data.csv')
paths = generate_monthly_report(df, 1, 2026)
print(f"Reports generated: {paths}")
```

---

## Success Indicators

You know you've mastered document formatting when:

- ✓ You can quickly identify the best format for any use case
- ✓ Your converted files open correctly in all target applications
- ✓ You maintain content integrity across all format transformations
- ✓ You've automated repetitive conversion tasks with scripts
- ✓ You understand the trade-offs between different formats
- ✓ You can troubleshoot format-specific issues efficiently
- ✓ Your multi-format documents maintain consistent branding
- ✓ You consider accessibility in all format choices
- ✓ You keep original source files organized and versioned
- ✓ You can explain format choices to non-technical stakeholders

---

## Related Skills

- [[Summarization]](../behavior-skills/summarization.md) - Condensing content for different formats
- [[Explanation]](../behavior-skills/explanation.md) - Communicating format choices clearly
- [[Planning]](../behavior-skills/planning.md) - Organizing multi-format documentation projects
- [[Style Adaptation]](../behavior-skills/style_adaptation.md) - Adjusting content tone per format

---

*This skill document itself demonstrates multi-format thinking by providing examples in various formats throughout.*
