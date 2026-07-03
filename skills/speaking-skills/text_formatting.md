# Text Formatting Skill

## Overview

Master the art of formatting text for clarity, emphasis, and structure using Markdown syntax. This skill enables you to create well-organized, readable documents that effectively communicate your message across different platforms and audiences. Whether you're writing documentation, creating README files, composing technical reports, or formatting messages in collaboration tools, proper text formatting enhances comprehension and professionalism.

## When to Use

- Writing technical documentation or README files
- Creating structured notes and knowledge base articles
- Composing formatted messages in Slack, Discord, or Teams
- Writing GitHub issues, pull requests, and commit messages
- Preparing blog posts or articles for static site generators
- Creating formatted emails that support Markdown
- Documenting code with clear structure and emphasis

## Core Text Formatting Elements

### Emphasis and Styling

#### Bold Text
**Purpose**: Highlight important terms, key concepts, or critical information.

**Syntax**: Wrap text with double asterisks `**` or double underscores `__`

```markdown
**This is bold text**
__Also bold text__
```

**Rendered**: **This is bold text**

**Best Practices**:
- ✅ Use sparingly for maximum impact
- ✅ Highlight key terms on first mention
- ✅ Emphasize action items or warnings
- ❌ Don't bold entire paragraphs (loses effectiveness)
- ❌ Avoid using for decorative purposes

**Use Cases**:
```markdown
**Important**: Always backup your data before proceeding.

The **primary key** uniquely identifies each record in a database table.

Please complete the following tasks by EOD:
- **High Priority**: Fix the authentication bug
- **Medium Priority**: Update documentation
```

---

#### Italic Text
**Purpose**: Add subtle emphasis, denote titles, or indicate foreign words.

**Syntax**: Wrap text with single asterisk `*` or single underscore `_`

```markdown
*This is italic text*
_Also italic text_
```

**Rendered**: *This is italic text*

**Best Practices**:
- ✅ Use for book/movie/article titles
- ✅ Emphasize words gently without shouting
- ✅ Indicate technical terms being defined
- ❌ Don't use for large blocks of text
- ❌ Avoid combining with bold excessively

**Use Cases**:
```markdown
Have you read *Clean Code* by Robert Martin?

The term *idempotent* means an operation can be performed multiple times without changing the result.

She said she was *very* excited about the launch.
```

---

#### Bold + Italic (Combined Emphasis)
**Purpose**: Maximum emphasis for critical information or strong highlights.

**Syntax**: Wrap text with triple asterisks `***` or triple underscores `___`

```markdown
***This is bold and italic***
___Also bold and italic___
```

**Rendered**: ***This is bold and italic***

**Best Practices**:
- ✅ Reserve for extremely important notices
- ✅ Use in callout boxes or warnings
- ❌ Avoid in regular prose (too distracting)
- ❌ Never use for entire sections

**Use Cases**:
```markdown
***WARNING***: This operation will delete all data permanently.

***Critical Security Update Required***: Please update immediately.
```

---

#### Strikethrough
**Purpose**: Show deleted content, indicate completed items, or mark outdated information.

**Syntax**: Wrap text with double tildes `~~`

```markdown
~~This text is struck through~~
```

**Rendered**: ~~This text is struck through~~

**Best Practices**:
- ✅ Show changes in changelogs
- ✅ Mark completed todo items
- ✅ Indicate deprecated features
- ❌ Don't use for emphasis (use bold instead)
- ❌ Avoid in formal documents

**Use Cases**:
```markdown
## Changelog
- ~~v1.0.0~~ (deprecated)
- v1.1.0 (current release)

## Todo List
- ~~Research competitors~~ ✓
- Draft initial design
- Review with team

The `old_method()` function is ~~deprecated~~ removed in v2.0.
```

---

### Headings and Hierarchy

#### Heading Levels
**Purpose**: Create document structure and enable navigation.

**Syntax**: Use hash symbols `#` (1-6 levels)

```markdown
# Heading 1 (Main Title)
## Heading 2 (Major Section)
### Heading 3 (Subsection)
#### Heading 4 (Minor Subsection)
##### Heading 5 (Detailed Point)
###### Heading 6 (Fine Detail)
```

**Best Practices**:
- ✅ Use only one H1 per document (the title)
- ✅ Maintain logical hierarchy (don't skip levels)
- ✅ Keep headings concise and descriptive
- ✅ Use sentence case or title case consistently
- ❌ Don't use headings just for font size
- ❌ Avoid overly long headings

**Document Structure Example**:
```markdown
# API Documentation

## Overview
Brief description of the API...

## Authentication
### API Keys
How to obtain and use API keys...

### OAuth 2.0
Setting up OAuth authentication...

## Endpoints
### Users
#### GET /users
Retrieve all users...

#### POST /users
Create a new user...

### Products
#### GET /products
List all products...

## Error Handling
Common error codes and solutions...

## Examples
Code samples and use cases...
```

**Accessibility Note**: Proper heading hierarchy enables screen readers to navigate documents effectively.

---

### Links

#### Basic Links
**Purpose**: Reference external resources, documentation, or related content.

**Syntax**: `[link text](URL)`

```markdown
[GitHub](https://github.com)
[Documentation](./docs/README.md)
```

**Rendered**: [GitHub](https://github.com)

**Best Practices**:
- ✅ Use descriptive link text (not "click here")
- ✅ Verify URLs are correct and accessible
- ✅ Consider adding context about the link destination
- ❌ Don't hide suspicious URLs behind vague text
- ❌ Avoid very long raw URLs in text

**Good vs Bad Examples**:
```markdown
❌ Bad: Click [here](https://example.com/docs) to read the documentation.

✅ Good: Read the [API Documentation](https://example.com/docs) for detailed usage instructions.

❌ Bad: Check out https://github.com/very-long-repository-url-that-breaks-formatting

✅ Good: View the [repository on GitHub](https://github.com/very-long-repository-url).
```

---

#### Links with Titles
**Purpose**: Add tooltips for additional context.

**Syntax**: `[link text](URL "optional title")`

```markdown
[MDN Web Docs](https://developer.mozilla.org "Mozilla Developer Network - Web Technology Documentation")
```

---

#### Reference-Style Links
**Purpose**: Improve readability when using multiple links or repeating URLs.

**Syntax**: Define links at the bottom of the document

```markdown
Check out [GitHub][gh] and [Stack Overflow][so] for help.

[gh]: https://github.com
[so]: https://stackoverflow.com
```

**Use Cases**:
```markdown
## Resources

For learning Python, I recommend:
- The official [Python Tutorial][python-tutorial]
- [Real Python][real-python] for practical guides
- [Python Weekly][python-weekly] newsletter

<!-- Link definitions -->
[python-tutorial]: https://docs.python.org/3/tutorial/
[real-python]: https://realpython.com
[python-weekly]: https://www.pythonweekly.com
```

---

### Lists

#### Unordered (Bullet) Lists
**Purpose**: Present items without specific order or priority.

**Syntax**: Use `-`, `*`, or `+` followed by a space

```markdown
- Item one
- Item two
- Item three
```

**Rendered**:
- Item one
- Item two
- Item three

**Best Practices**:
- ✅ Use for non-sequential items
- ✅ Keep list items parallel in structure
- ✅ Be consistent with bullet character throughout document
- ❌ Don't mix bullet styles arbitrarily
- ❌ Avoid single-item lists

**Example**:
```markdown
## Features
- Fast performance
- Easy to use
- Cross-platform support
- Extensive documentation
```

---

#### Ordered (Numbered) Lists
**Purpose**: Show sequential steps, rankings, or prioritized items.

**Syntax**: Use numbers followed by a period and space

```markdown
1. First step
2. Second step
3. Third step
```

**Rendered**:
1. First step
2. Second step
3. Third step

**Best Practices**:
- ✅ Use for procedures and tutorials
- ✅ Start from 1 (Markdown auto-numbers)
- ✅ Keep steps atomic and actionable
- ❌ Don't use for non-sequential items
- ❌ Avoid nested numbered lists (can be confusing)

**Example**:
```markdown
## Installation Steps

1. Download the installer from the website
2. Run the installer executable
3. Accept the license agreement
4. Choose installation directory
5. Click "Install" and wait for completion
6. Launch the application
```

**Pro Tip**: You can use `1.` for all items; Markdown will auto-number:
```markdown
1. Step one
1. Step two
1. Step three
```

---

#### Nested Lists
**Purpose**: Show hierarchical relationships between items.

**Syntax**: Indent sub-items with 2 or 4 spaces

```markdown
- Parent item
  - Child item 1
  - Child item 2
    - Grandchild item
- Another parent item
```

**Rendered**:
- Parent item
  - Child item 1
  - Child item 2
    - Grandchild item
- Another parent item

**Example**:
```markdown
## Project Structure
- src/
  - components/
    - Button.js
    - Modal.js
  - utils/
    - helpers.js
    - constants.js
- tests/
  - unit/
  - integration/
- docs/
```

---

#### Task Lists (Checkboxes)
**Purpose**: Track progress, create todo lists, manage action items.

**Syntax**: Use `- [ ]` for incomplete, `- [x]` for complete

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another pending task
```

**Rendered**: 
- [x] Completed task
- [ ] Incomplete task
- [ ] Another pending task

**Best Practices**:
- ✅ Use for sprint planning and tracking
- ✅ Break large tasks into smaller checkboxes
- ✅ Update status regularly
- ❌ Don't leave outdated checklists
- ❌ Avoid too many nested checkboxes

**Example**:
```markdown
## Sprint Goals

### Backend Development
- [x] Set up database schema
- [x] Implement user authentication
- [ ] Create API endpoints
  - [ ] User CRUD operations
  - [ ] Product management
  - [ ] Order processing
- [ ] Write unit tests
- [ ] Deploy to staging

### Frontend Development
- [ ] Design component library
- [ ] Implement responsive layout
- [ ] Connect to backend APIs
```

---

### Code Formatting

#### Inline Code
**Purpose**: Highlight code snippets, commands, variables, or file paths within text.

**Syntax**: Wrap text with single backticks `` ` ``

```markdown
Use the `print()` function to output text.
Set the `NODE_ENV` environment variable.
Edit the `config.json` file.
```

**Rendered**: Use the `print()` function to output text.

**Best Practices**:
- ✅ Use for function names, variables, commands
- ✅ Highlight file names and paths
- ✅ Denote keyboard shortcuts
- ❌ Don't use for emphasis (use bold/italic)
- ❌ Avoid for multi-line code (use code blocks)

**Examples**:
```markdown
Call the `getUserById(id)` method to retrieve user data.

The configuration is stored in `~/.config/app/settings.yaml`.

Press `Ctrl+C` to copy and `Ctrl+V` to paste.

Set the `DEBUG=true` flag to enable verbose logging.
```

---

#### Code Blocks
**Purpose**: Display multi-line code with proper formatting and syntax highlighting.

**Syntax**: Wrap code with triple backticks ``` and optionally specify language

````markdown
```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Usage
message = greet("World")
print(message)
```
````

**Rendered**:
```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Usage
message = greet("World")
print(message)
```

**Supported Languages** (common ones):
- `python`, `javascript`, `typescript`, `java`, `cpp`, `csharp`
- `bash`, `sh`, `zsh`, `powershell`
- `html`, `css`, `scss`, `less`
- `sql`, `json`, `yaml`, `xml`, `toml`
- `markdown`, `latex`, `ruby`, `go`, `rust`, `swift`

**Best Practices**:
- ✅ Always specify the language for syntax highlighting
- ✅ Keep code blocks focused and concise
- ✅ Add comments explaining complex logic
- ✅ Include expected output when relevant
- ❌ Don't include unnecessary code
- ❌ Avoid screenshots of code (not searchable/copyable)

**Example with Output**:
````markdown
```bash
$ npm install express
added 47 packages in 3s

$ node server.js
Server running on http://localhost:3000
```
````

---

#### Indented Code Blocks
**Purpose**: Alternative syntax for code blocks (older Markdown style).

**Syntax**: Indent code by 4 spaces or 1 tab

```markdown
    def old_style():
        print("This also works but is less common")
```

**Note**: Fenced code blocks (triple backticks) are preferred for clarity and language specification.

---

### Blockquotes

#### Basic Blockquotes
**Purpose**: Highlight quotations, callouts, or important notes.

**Syntax**: Prefix lines with `>`

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> Separate paragraphs with blank lines.
```

**Rendered**:
> This is a blockquote.
> It can span multiple lines.
>
> Separate paragraphs with blank lines.

**Best Practices**:
- ✅ Use for quoting documentation or sources
- ✅ Highlight important notes or tips
- ✅ Create visual separation for asides
- ❌ Don't overuse (loses impact)
- ❌ Avoid for regular paragraph text

---

#### Nested Blockquotes
**Purpose**: Show quoted text within quoted text or multi-level responses.

**Syntax**: Add multiple `>` symbols

```markdown
> Original statement
>
>> Response to original
>>
>>> Further reply
```

**Rendered**:
> Original statement
>
>> Response to original
>
>>> Further reply

---

#### Blockquotes with Other Elements
**Purpose**: Combine blockquotes with formatting for rich callouts.

```markdown
> **Note**: This is an important announcement.
>
> Please review the following:
> - Item one
> - Item two
>
> For more details, see the [documentation](https://example.com).
```

**Rendered**:
> **Note**: This is an important announcement.
>
> Please review the following:
> - Item one
> - Item two
>
> For more details, see the [documentation](https://example.com).

---

### Tables

#### Basic Tables
**Purpose**: Organize and present structured data clearly.

**Syntax**: Use pipes `|` and dashes `-` for headers

```markdown
| Name | Role | Experience |
|------|------|------------|
| Alice | Developer | 5 years |
| Bob | Designer | 3 years |
| Carol | Manager | 8 years |
```

**Rendered**:

| Name | Role | Experience |
|------|------|------------|
| Alice | Developer | 5 years |
| Bob | Designer | 3 years |
| Carol | Manager | 8 years |

**Alignment Syntax**:
```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| L1 | C1 | R1 |
| L2 | C2 | R2 |
```

- `:---` or `:-----` = Left aligned (default)
- `:---:` or `:----:` = Center aligned
- `---:` or `----:` = Right aligned

**Best Practices**:
- ✅ Use for comparative data or specifications
- ✅ Keep columns focused and related
- ✅ Align numbers to the right for readability
- ✅ Keep header names short and clear
- ❌ Don't use for layout purposes
- ❌ Avoid tables with many empty cells
- ❌ Don't create overly wide tables

**Example**:
```markdown
## API Endpoints

| Method | Endpoint | Description | Auth Required |
|:-------|:---------|:------------|:--------------|
| GET | `/users` | List all users | Yes |
| POST | `/users` | Create user | Yes |
| GET | `/users/:id` | Get user by ID | Yes |
| PUT | `/users/:id` | Update user | Yes |
| DELETE | `/users/:id` | Delete user | Yes |
```

---

### Horizontal Rules

**Purpose**: Visually separate sections of content.

**Syntax**: Use three or more dashes `---`, asterisks `***`, or underscores `___`

```markdown
Section one content.

---

Section two content.
```

**Best Practices**:
- ✅ Use to separate major sections
- ✅ Create visual breaks in long documents
- ❌ Don't overuse (creates clutter)
- ❌ Avoid using multiple in succession

---

### Escaping Characters

**Purpose**: Display literal Markdown characters without formatting.

**Syntax**: Prefix with backslash `\`

```markdown
\*\*Not bold\*\*
\# Not a heading
\[Not a link\](url)
\`Not code\`
```

**Rendered**: \*\*Not bold\*\*

**Common Characters to Escape**:
- `\` Backslash itself
- `` \` `` Backtick
- `*` Asterisk
- `_` Underscore
- `{}` Curly braces
- `[]` Brackets
- `()` Parentheses
- `#` Hash
- `+` Plus
- `-` Hyphen (at start of line)
- `.` Period (at start of line)
- `!` Exclamation mark

**Example**:
```markdown
To create bold text, wrap it in double asterisks: \*\*bold\*\*

The command uses special characters: grep \[a-z\]\* file.txt
```

---

## Advanced Formatting Techniques

### Emoji Integration
**Purpose**: Add visual cues and emotional context.

```markdown
✅ Task completed
❌ Task failed
⚠️ Warning
💡 Tip
🎉 Celebration
📝 Note
```

**Best Practices**:
- ✅ Use sparingly for emphasis
- ✅ Ensure accessibility (screen readers read emoji)
- ✅ Be culturally sensitive
- ❌ Don't rely on emoji alone for meaning
- ❌ Avoid in formal documentation

---

### HTML in Markdown
**Purpose**: Access formatting not available in standard Markdown.

```markdown
<details>
<summary>Click to expand</summary>

Hidden content here...

</details>

<span style="color: red">Red text</span>

<kbd>Ctrl</kbd> + <kbd>C</kbd>
```

**Note**: Not all Markdown processors support HTML. Use cautiously.

---

### Definition Lists
**Purpose**: Create glossary-style definitions (supported in some flavors).

```markdown
Term One
: Definition of term one

Term Two
: Definition of term two
: Additional definition
```

---

## Common Formatting Patterns

### Documentation Headers
```markdown
# Feature Name

> **Status**: <!-- Status badge or text -->
> **Version**: 1.0.0
> **Last Updated**: 2024-01-15

## Overview
Brief description...

## Prerequisites
- Requirement 1
- Requirement 2

## Quick Start
1. Step one
2. Step two
3. Step three

## Configuration
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `port` | number | 3000 | Server port |

## Examples
\`\`\`javascript
// Example code
\`\`\`

## Troubleshooting
### Common Issues
- **Issue**: Description
  - **Solution**: Fix

## Related Resources
- [Link 1](url)
- [Link 2](url)
```

---

### Pull Request Templates
```markdown
## Description
<!-- What does this PR do? -->

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added where needed
- [ ] Documentation updated

## Screenshots (if applicable)
<!-- Add screenshots here -->

## Related Issues
Closes #123
```

---

### Meeting Notes Template
```markdown
# Meeting Notes: [Topic]

**Date**: YYYY-MM-DD  
**Attendees**: @person1, @person2, @person3  
**Absent**: @person4  

## Agenda
1. Topic one
2. Topic two
3. Topic three

## Discussion Notes

### Topic One
Key points discussed...

**Decision**: What was decided

### Topic Two
Key points discussed...

## Action Items
- [ ] @person1 - Task description (Due: date)
- [ ] @person2 - Task description (Due: date)

## Next Meeting
**Date**: YYYY-MM-DD  
**Agenda Items**: 
- Item 1
- Item 2
```

---

## Accessibility Considerations

### Screen Reader Compatibility
- Use proper heading hierarchy (H1 → H2 → H3)
- Write descriptive link text
- Add alt text to images: `![Description](image.png)`
- Use lists for list content (not manual numbering)
- Ensure sufficient color contrast (when using HTML/CSS)

### Readability Best Practices
- Keep paragraphs short (3-5 sentences)
- Use white space effectively
- Break up long sections with subheadings
- Use bulleted lists for multiple items
- Avoid walls of text

### Mobile-Friendly Formatting
- Keep line lengths reasonable (< 80 characters in source)
- Test tables on small screens
- Avoid overly complex nested structures
- Use responsive images

---

## Common Pitfalls and Solutions

### Pitfall 1: Inconsistent Formatting
**Problem**: Mixing different styles throughout document.

**Solution**: Create and follow a style guide:
```markdown
## Style Guide
- Use ATX headings (#) not Setext (===)
- Use - for unordered lists
- Use ``` fenced code blocks
- Use ** for bold, * for italic
- Keep line length under 80 characters
```

---

### Pitfall 2: Broken Links
**Problem**: Links that lead nowhere or to wrong places.

**Solution**: 
- ✅ Test all links before publishing
- ✅ Use relative paths for internal links
- ✅ Consider automated link checking tools
- ✅ Update links when content moves

**Tools**:
- `markdown-link-check` (CLI)
- GitHub's built-in link checker
- Online validators

---

### Pitfall 3: Over-Formatting
**Problem**: Too much bold, italic, or other emphasis.

**Solution**: 
- Follow the 80/20 rule: 80% plain text, 20% formatted
- Ask: "Does this formatting add value?"
- Get feedback from others
- Remember: if everything is emphasized, nothing is

---

### Pitfall 4: Platform Incompatibility
**Problem**: Formatting that works in one place but not another.

**Solution**:
- Know your platform's Markdown flavor (GitHub, GitLab, CommonMark, etc.)
- Test on target platforms
- Stick to CommonMark for maximum compatibility
- Document any platform-specific features used

---

### Pitfall 5: Poor Table Formatting
**Problem**: Tables that are hard to read or maintain.

**Solution**:
```markdown
<!-- Bad: Misaligned and hard to read in source -->
|Name|Age|City|
|-|-|-|
|John|30|NYC|
|Jane|25|LA|

<!-- Good: Aligned columns in source -->
| Name | Age | City |
|------|-----|------|
| John | 30  | NYC  |
| Jane | 25  | LA   |
```

---

## Tools and Resources

### Editors with Markdown Support
- **VS Code**: Excellent Markdown preview and extensions
- **Typora**: WYSIWYG Markdown editor
- **Obsidian**: Knowledge base with Markdown
- **iA Writer**: Distraction-free writing
- **Notion**: Collaborative workspace with Markdown

### Useful Extensions/Plugins
- **Markdown All in One** (VS Code)
- **Markdown Preview Enhanced** (VS Code)
- **Prettier**: Auto-formatting
- **markdownlint**: Style checking

### Conversion Tools
- **Pandoc**: Universal document converter
- **Marked**: Markdown to HTML
- **mdpdf**: Markdown to PDF

### Validation Tools
- **markdownlint**: Linting and style checking
- **remark-lint**: Configurable linter
- **CommonMark spec**: Official specification reference

---

## Practice Exercises

### Exercise 1: Format a Plain Text Document
Take a plain text document and add appropriate formatting:
- Add headings for sections
- Emphasize key terms
- Convert lists to proper Markdown lists
- Add code blocks for any code snippets

### Exercise 2: Create a README
Write a README file for a project including:
- Project title and description
- Installation instructions (numbered list)
- Usage examples (code blocks)
- Contributing guidelines
- License information

### Exercise 3: Build a Comparison Table
Create a table comparing 3-5 similar tools or technologies with:
- At least 4 columns
- Mixed data types (text, numbers, booleans)
- Proper alignment

### Exercise 4: Write a Tutorial
Create a step-by-step tutorial with:
- Clear heading hierarchy
- Numbered steps
- Code examples
- Tips and warnings (blockquotes)
- Links to resources

---

## Success Indicators

You've mastered text formatting when you can:

✅ Create well-structured documents that are easy to scan  
✅ Choose the right formatting element for each purpose  
✅ Maintain consistency throughout long documents  
✅ Adapt formatting to different Markdown flavors  
✅ Make documents accessible to all users  
✅ Balance visual appeal with readability  
✅ Debug formatting issues quickly  
✅ Teach formatting best practices to others  

---

## Quick Reference Card

```markdown
# Quick Reference

## Emphasis
**bold** or __bold__
*italic* or _italic_
***bold italic***
~~strikethrough~~

## Headings
# H1
## H2
### H3

## Links
[text](url)
[text](url "title")

## Images
![alt](url)

## Code
`inline`
```language
code block
```

## Lists
- Bullet
1. Numbered
- [ ] Task

## Quotes
> Blockquote

## Tables
| Header | Header |
|--------|--------|
| Cell   | Cell   |

## Rules
--- or *** or ___
```

---

## Final Tips

1. **Consistency is Key**: Pick a style and stick with it throughout your document.

2. **Preview Before Publishing**: Always check how your Markdown renders.

3. **Less is More**: Use formatting to enhance, not overwhelm.

4. **Know Your Audience**: Formal docs need different formatting than casual notes.

5. **Learn Keyboard Shortcuts**: Most editors have shortcuts for common formatting.

6. **Use Snippets**: Create templates for frequently used patterns.

7. **Stay Updated**: Markdown evolves; new features appear in different flavors.

8. **Practice Regularly**: The more you use Markdown, the more natural it becomes.

Remember: Good formatting is invisible—it makes content easier to consume without drawing attention to itself.
```python
print("Hello")
Quotes

Use > to create a quote.

Example:

> This is a quote

Result:

This is a quote

Horizontal Lines

Use three dashes to create a separator.

Example:

---

Result:
Use these formatting tools to improve readability, organize information, and make text easier to understand.