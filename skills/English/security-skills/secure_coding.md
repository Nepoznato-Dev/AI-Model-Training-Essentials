# Secure Coding

## Overview

Secure coding is the practice of writing software code that is resistant to attacks and vulnerabilities. It involves understanding common security threats, implementing defensive programming techniques, and following established security guidelines throughout the development lifecycle.

This skill covers fundamental security principles, common vulnerability patterns, and practical techniques for writing secure code.

## Core Competencies

- **Threat Modeling**: Identifying potential security threats in system design
- **Input Validation**: Sanitizing and validating all external inputs
- **Authentication & Authorization**: Implementing secure access control
- **Cryptography**: Proper use of encryption and hashing
- **Session Management**: Secure handling of user sessions
- **Error Handling**: Preventing information leakage through errors
- **Dependency Security**: Managing third-party library risks
- **Security Testing**: Identifying vulnerabilities through testing

## When to Use

Secure coding practices should be applied:
- ✅ In all production code without exception
- ✅ When handling sensitive data (PII, financial, health)
- ✅ When building authentication/authorization systems
- ✅ When processing user inputs
- ✅ When integrating with external services
- ✅ When storing or transmitting sensitive information

**Security is not optional** - it should be integrated into every stage of development.

## OWASP Top 10 Vulnerabilities

```
┌─────────────────────────────────────────────────────────────────┐
│                    OWASP Top 10 (2021)                          │
├─────────────────────────────────────────────────────────────────┤
│ 1. Broken Access Control           ████████████████████  94%    │
│ 2. Cryptographic Failures          ████████████████      86%    │
│ 3. Injection                       ███████████████       84%    │
│ 4. Insecure Design                 █████████████         78%    │
│ 5. Security Misconfiguration       █████████████         76%    │
│ 6. Vulnerable Components           ████████████          70%    │
│ 7. Authentication Failures         ████████████          68%    │
│ 8. Software & Data Integrity       ██████████            62%    │
│ 9. Security Logging Failures       █████████             58%    │
│ 10. Server-Side Request Forgery    ████████              54%    │
└─────────────────────────────────────────────────────────────────┘
```

## Practical Templates

### Input Validation Template

```javascript
// validators/inputValidator.js
const validator = require('validator');
const { sanitizeHtml } = require('sanitize-html');

class InputValidator {
  // Email validation
  static validateEmail(email) {
    if (!email || typeof email !== 'string') {
      throw new ValidationError('Email is required');
    }
    
    const normalizedEmail = email.toLowerCase().trim();
    
    if (!validator.isEmail(normalizedEmail)) {
      throw new ValidationError('Invalid email format');
    }
    
    if (normalizedEmail.length > 255) {
      throw new ValidationError('Email too long');
    }
    
    return normalizedEmail;
  }

  // Username validation
  static validateUsername(username) {
    if (!username || typeof username !== 'string') {
      throw new ValidationError('Username is required');
    }
    
    const trimmed = username.trim();
    
    if (trimmed.length < 3 || trimmed.length > 30) {
      throw new ValidationError('Username must be 3-30 characters');
    }
    
    if (!/^[a-zA-Z0-9_-]+$/.test(trimmed)) {
      throw new ValidationError('Username can only contain letters, numbers, underscore, and hyphen');
    }
    
    return trimmed;
  }

  // HTML sanitization
  static sanitizeUserContent(content) {
    return sanitizeHtml(content, {
      allowedTags: ['b', 'i', 'em', 'strong', 'p', 'br', 'ul', 'ol', 'li'],
      allowedAttributes: {},
      disallowedTagsMode: 'discard'
    });
  }

  // SQL injection prevention
  static validateId(id, type = 'uuid') {
    if (!id) {
      throw new ValidationError('ID is required');
    }
    
    if (type === 'uuid' && !validator.isUUID(id)) {
      throw new ValidationError('Invalid ID format');
    }
    
    if (type === 'integer' && !validator.isInt(id.toString())) {
      throw new ValidationError('Invalid ID format');
    }
    
    return id;
  }
}

class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = 'ValidationError';
    this.statusCode = 400;
  }
}

module.exports = { InputValidator, ValidationError };
```

### Authentication Template

```javascript
// auth/authentication.js
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const crypto = require('crypto');

class AuthenticationService {
  constructor(config) {
    this.jwtSecret = config.jwtSecret;
    this.jwtExpiry = config.jwtExpiry || '1h';
    this.saltRounds = 12;
    this.maxLoginAttempts = 5;
    this.lockoutDuration = 15 * 60 * 1000; // 15 minutes
  }

  // Secure password hashing
  async hashPassword(password) {
    const salt = await bcrypt.genSalt(this.saltRounds);
    return await bcrypt.hash(password, salt);
  }

  // Password verification
  async verifyPassword(password, hash) {
    return await bcrypt.compare(password, hash);
  }

  // Password strength validation
  validatePasswordStrength(password) {
    const errors = [];
    
    if (password.length < 12) {
      errors.push('Password must be at least 12 characters');
    }
    
    if (!/[A-Z]/.test(password)) {
      errors.push('Password must contain an uppercase letter');
    }
    
    if (!/[a-z]/.test(password)) {
      errors.push('Password must contain a lowercase letter');
    }
    
    if (!/[0-9]/.test(password)) {
      errors.push('Password must contain a number');
    }
    
    if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
      errors.push('Password must contain a special character');
    }
    
    // Check against common passwords
    const commonPasswords = ['password', '123456', 'qwerty'];
    if (commonPasswords.includes(password.toLowerCase())) {
      errors.push('Password is too common');
    }
    
    return {
      isValid: errors.length === 0,
      errors
    };
  }

  // Generate JWT token
  generateToken(payload, additionalClaims = {}) {
    const tokenPayload = {
      ...payload,
      iat: Math.floor(Date.now() / 1000),
      jti: crypto.randomBytes(16).toString('hex'),
      ...additionalClaims
    };
    
    return jwt.sign(tokenPayload, this.jwtSecret, {
      expiresIn: this.jwtExpiry,
      algorithm: 'HS256'
    });
  }

  // Verify JWT token
  verifyToken(token) {
    try {
      const decoded = jwt.verify(token, this.jwtSecret, {
        algorithms: ['HS256']
      });
      
      // Check for token reuse (implement with Redis or similar)
      // if (await this.isTokenBlacklisted(decoded.jti)) {
      //   throw new Error('Token has been revoked');
      // }
      
      return decoded;
    } catch (error) {
      if (error.name === 'TokenExpiredError') {
        throw new Error('Token has expired');
      }
      if (error.name === 'JsonWebTokenError') {
        throw new Error('Invalid token');
      }
      throw error;
    }
  }

  // Refresh token rotation
  async rotateRefreshToken(oldToken, userId) {
    const decoded = this.verifyToken(oldToken);
    
    if (decoded.userId !== userId) {
      throw new Error('Invalid refresh token');
    }
    
    // Invalidate old token
    await this.blacklistToken(decoded.jti);
    
    // Generate new token
    return this.generateToken(
      { userId: decoded.userId },
      { type: 'refresh' }
    );
  }

  // Rate limiting for login attempts
  async checkLoginAttempts(identifier) {
    const attempts = await this.getLoginAttempts(identifier);
    
    if (attempts >= this.maxLoginAttempts) {
      const lastAttempt = await this.getLastAttemptTime(identifier);
      const lockoutEnd = lastAttempt + this.lockoutDuration;
      
      if (Date.now() < lockoutEnd) {
        const remainingTime = Math.ceil((lockoutEnd - Date.now()) / 60000);
        throw new Error(`Account locked. Try again in ${remainingTime} minutes`);
      }
      
      // Reset attempts after lockout period
      await this.resetLoginAttempts(identifier);
    }
  }

  async recordLoginAttempt(identifier, success) {
    if (success) {
      await this.resetLoginAttempts(identifier);
    } else {
      await this.incrementLoginAttempts(identifier);
    }
  }

  // Placeholder methods - implement with your data store
  async blacklistToken(jti) { /* Implement with Redis */ }
  async isTokenBlacklisted(jti) { /* Implement with Redis */ }
  async getLoginAttempts(identifier) { /* Implement with DB */ }
  async incrementLoginAttempts(identifier) { /* Implement with DB */ }
  async resetLoginAttempts(identifier) { /* Implement with DB */ }
  async getLastAttemptTime(identifier) { /* Implement with DB */ }
}

module.exports = { AuthenticationService };
```

### Authorization Template (RBAC)

```javascript
// auth/authorization.js
class AuthorizationService {
  constructor() {
    this.roles = new Map();
    this.permissions = new Map();
  }

  // Define roles and permissions
  initializeRoles() {
    this.roles.set('admin', {
      level: 100,
      permissions: ['*']
    });
    
    this.roles.set('manager', {
      level: 50,
      permissions: [
        'users:read',
        'users:create',
        'users:update',
        'reports:read',
        'reports:create'
      ]
    });
    
    this.roles.set('user', {
      level: 10,
      permissions: [
        'users:read:own',
        'profile:update:own'
      ]
    });
  }

  // Check if user has permission
  hasPermission(user, permission, resource = null) {
    const role = this.roles.get(user.role);
    
    if (!role) {
      return false;
    }
    
    // Wildcard permission
    if (role.permissions.includes('*')) {
      return true;
    }
    
    // Direct permission match
    if (role.permissions.includes(permission)) {
      return true;
    }
    
    // Resource-specific permission (e.g., users:read:own)
    const [action, scope] = permission.split(':');
    if (scope === 'own' && resource) {
      return resource.ownerId === user.id;
    }
    
    return false;
  }

  // Middleware for Express
  requirePermission(permission) {
    return (req, res, next) => {
      if (!req.user) {
        return res.status(401).json({ error: 'Unauthorized' });
      }
      
      if (!this.hasPermission(req.user, permission, req.resource)) {
        return res.status(403).json({ 
          error: 'Forbidden',
          message: 'Insufficient permissions'
        });
      }
      
      next();
    };
  }

  // Hierarchical role check
  hasRoleLevel(user, minimumLevel) {
    const role = this.roles.get(user.role);
    return role && role.level >= minimumLevel;
  }
}

module.exports = { AuthorizationService };
```

### Secure Database Query Template

```javascript
// database/secureQueries.js
const { Pool } = require('pg');

class SecureDatabase {
  constructor(connectionConfig) {
    this.pool = new Pool(connectionConfig);
  }

  // ✅ GOOD: Parameterized queries prevent SQL injection
  async getUserById(userId) {
    const query = 'SELECT * FROM users WHERE id = $1 AND active = $2';
    const values = [userId, true];
    
    const result = await this.pool.query(query, values);
    return result.rows[0];
  }

  // ✅ GOOD: Using query builder with parameterization
  async searchUsers(searchTerm, limit = 10) {
    const query = `
      SELECT id, username, email, created_at 
      FROM users 
      WHERE username ILIKE $1 
        AND active = $2
      LIMIT $3
    `;
    const values = [`%${searchTerm}%`, true, limit];
    
    const result = await this.pool.query(query, values);
    return result.rows;
  }

  // ✅ GOOD: Transaction with proper error handling
  async transferFunds(fromUserId, toUserId, amount) {
    const client = await this.pool.connect();
    
    try {
      await client.query('BEGIN');
      
      // Check balance
      const balanceResult = await client.query(
        'SELECT balance FROM accounts WHERE user_id = $1 FOR UPDATE',
        [fromUserId]
      );
      
      if (balanceResult.rows[0].balance < amount) {
        throw new Error('Insufficient funds');
      }
      
      // Debit sender
      await client.query(
        'UPDATE accounts SET balance = balance - $1 WHERE user_id = $2',
        [amount, fromUserId]
      );
      
      // Credit receiver
      await client.query(
        'UPDATE accounts SET balance = balance + $1 WHERE user_id = $2',
        [amount, toUserId]
      );
      
      // Log transaction
      await client.query(
        `INSERT INTO transactions (sender_id, receiver_id, amount, created_at)
         VALUES ($1, $2, $3, NOW())`,
        [fromUserId, toUserId, amount]
      );
      
      await client.query('COMMIT');
      return { success: true };
      
    } catch (error) {
      await client.query('ROLLBACK');
      
      // Log error securely (don't expose details to user)
      console.error('Transaction failed:', error.code);
      
      throw new Error('Transaction failed. Please try again.');
    } finally {
      client.release();
    }
  }

  // ❌ BAD: Never concatenate user input into queries
  // async getUserUnsafe(userId) {
  //   const query = `SELECT * FROM users WHERE id = ${userId}`;
  //   return await this.pool.query(query);
  // }
}

module.exports = { SecureDatabase };
```

## Common Pitfalls

### 🚫 Security Anti-Patterns

1. **SQL Injection**
   ```javascript
   // ❌ BAD: String concatenation
   const query = `SELECT * FROM users WHERE email = '${email}'`;
   
   // ✅ GOOD: Parameterized query
   const query = 'SELECT * FROM users WHERE email = $1';
   const values = [email];
   ```

2. **XSS (Cross-Site Scripting)**
   ```javascript
   // ❌ BAD: Rendering user input directly
   res.send(`<div>${userComment}</div>`);
   
   // ✅ GOOD: Sanitize or escape output
   res.send(`<div>${escapeHtml(userComment)}</div>`);
   ```

3. **Hard-Coded Secrets**
   ```javascript
   // ❌ BAD: Secrets in code
   const API_KEY = 'sk_live_abc123xyz';
   
   // ✅ GOOD: Environment variables
   const API_KEY = process.env.API_KEY;
   ```

4. **Weak Password Hashing**
   ```javascript
   // ❌ BAD: MD5 or SHA1
   const hash = crypto.createHash('md5').update(password).digest('hex');
   
   // ✅ GOOD: bcrypt or argon2
   const hash = await bcrypt.hash(password, 12);
   ```

5. **Insecure Direct Object Reference**
   ```javascript
   // ❌ BAD: No authorization check
   app.get('/api/users/:id', async (req, res) => {
     const user = await db.getUser(req.params.id);
     res.json(user);
   });
   
   // ✅ GOOD: Verify ownership
   app.get('/api/users/:id', async (req, res) => {
     const user = await db.getUser(req.params.id);
     if (user.ownerId !== req.user.id) {
       return res.status(403).json({ error: 'Forbidden' });
     }
     res.json(user);
   });
   ```

6. **Sensitive Data in Logs**
   ```javascript
   // ❌ BAD: Logging sensitive information
   console.log('User login:', { email, password });
   
   // ✅ GOOD: Log only necessary information
   console.log('User login attempt:', { 
     email: maskEmail(email), 
     timestamp: new Date().toISOString(),
     ip: req.ip 
   });
   ```

7. **Missing HTTPS**
   ```javascript
   // ❌ BAD: HTTP only
   app.listen(3000);
   
   // ✅ GOOD: Force HTTPS
   app.use((req, res, next) => {
     if (!req.secure && process.env.NODE_ENV === 'production') {
       return res.redirect(`https://${req.headers.host}${req.url}`);
     }
     next();
   });
   ```

8. **Verbose Error Messages**
   ```javascript
   // ❌ BAD: Exposing stack traces
   app.use((err, req, res, next) => {
     res.status(500).send(err.stack);
   });
   
   // ✅ GOOD: Generic error messages
   app.use((err, req, res, next) => {
     console.error('Error:', err);
     res.status(500).json({ 
       error: 'Internal server error',
       requestId: req.id 
     });
   });
   ```

## Best Practices

### ✅ Secure Coding Guidelines

1. **Defense in Depth**
   - Multiple layers of security
   - Don't rely on a single control
   - Validate at every boundary

2. **Principle of Least Privilege**
   - Grant minimum necessary permissions
   - Use separate accounts for different functions
   - Regularly review and revoke access

3. **Fail Securely**
   - Default to deny
   - Don't leak information in errors
   - Maintain availability during attacks

4. **Never Trust User Input**
   - Validate all inputs
   - Sanitize before output
   - Use allowlists over blocklists

5. **Keep Dependencies Updated**
   - Regularly audit dependencies
   - Use automated security scanning
   - Subscribe to security advisories

6. **Use Established Libraries**
   - Don't roll your own crypto
   - Use well-maintained security libraries
   - Follow implementation guides

7. **Implement Proper Logging**
   - Log security events
   - Don't log sensitive data
   - Monitor for anomalies

8. **Regular Security Reviews**
   - Code reviews with security focus
   - Penetration testing
   - Threat modeling sessions

## Tools & Resources

### Security Scanning Tools

| Category | Tools |
|----------|-------|
| **SAST** | SonarQube, Semgrep, CodeQL, Snyk Code |
| **DAST** | OWASP ZAP, Burp Suite, Nikto |
| **Dependency** | npm audit, Snyk, Dependabot, Renovate |
| **Container** | Trivy, Clair, Docker Scan |
| **Secret Detection** | GitLeaks, TruffleHog, Detectify |

### Security Libraries

| Language | Libraries |
|----------|-----------|
| **Node.js** | helmet, cors, express-rate-limit, bcrypt |
| **Python** | cryptography, passlib, bleach, safety |
| **Java** | Spring Security, Bouncy Castle, OWASP ESAPI |
| **Go** | golang.org/x/crypto, go-jose |

### Learning Resources

- 📚 ["Secure by Design" by Dan Bergh Johnsson](https://www.manning.com/books/secure-by-design)
- 📚 ["The Web Application Hacker's Handbook"](https://www.wiley.com/en-us/The+Web+Application+Hacker's+Handbook%3A+Finding+and+Exploiting+Security+Flaws%2C+2nd+Edition-p-9781118026472)
- 🌐 [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- 🌐 [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- 🌐 [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- 🎥 [PortSwigger Web Security Academy](https://portswigger.net/web-security)

## Examples

### Example 1: Secure API Endpoint

```javascript
// routes/users.js
const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { InputValidator } = require('../validators/inputValidator');
const { AuthenticationService } = require('../auth/authentication');
const { AuthorizationService } = require('../auth/authorization');
const { SecureDatabase } = require('../database/secureQueries');

const router = express.Router();
const authService = new AuthenticationService(process.env);
const authzService = new AuthorizationService();
const db = new SecureDatabase(process.env.DATABASE_URL);

// Security headers
router.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: { error: 'Too many requests, please try again later' }
});
router.use(limiter);

// Create user endpoint
router.post('/users', async (req, res) => {
  const requestId = crypto.randomUUID();
  
  try {
    // Validate input
    const { email, password, username } = req.body;
    
    const validatedEmail = InputValidator.validateEmail(email);
    const validatedUsername = InputValidator.validateUsername(username);
    
    // Check password strength
    const passwordValidation = authService.validatePasswordStrength(password);
    if (!passwordValidation.isValid) {
      return res.status(400).json({
        requestId,
        errors: passwordValidation.errors
      });
    }
    
    // Check if user exists
    const existingUser = await db.getUserByEmail(validatedEmail);
    if (existingUser) {
      return res.status(409).json({
        requestId,
        error: 'User already exists'
      });
    }
    
    // Hash password and create user
    const passwordHash = await authService.hashPassword(password);
    const user = await db.createUser({
      email: validatedEmail,
      username: validatedUsername,
      passwordHash
    });
    
    // Log creation (without sensitive data)
    console.log('User created:', {
      userId: user.id,
      timestamp: new Date().toISOString(),
      requestId
    });
    
    res.status(201).json({
      requestId,
      user: {
        id: user.id,
        email: user.email,
        username: user.username,
        createdAt: user.createdAt
      }
    });
    
  } catch (error) {
    console.error('User creation failed:', {
      requestId,
      errorCode: error.code
    });
    
    res.status(error.statusCode || 500).json({
      requestId,
      error: error.message || 'An error occurred'
    });
  }
});

module.exports = router;
```

### Example 2: Security Headers Configuration

```javascript
// middleware/securityHeaders.js
const helmet = require('helmet');

function configureSecurityHeaders(app) {
  // Content Security Policy
  const cspDirectives = {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'"],
    styleSrc: ["'self'", "'unsafe-inline'", 'https://fonts.googleapis.com'],
    imgSrc: ["'self'", 'data:', 'https:'],
    fontSrc: ["'self'", 'https://fonts.gstatic.com'],
    connectSrc: ["'self'", 'https://api.example.com'],
    frameAncestors: ["'none'"],
    baseUri: ["'self'"],
    formAction: ["'self'"]
  };

  app.use(helmet.contentSecurityPolicy({
    directives: cspDirectives
  }));

  // Other security headers
  app.use(helmet.crossOriginEmbedderPolicy());
  app.use(helmet.crossOriginOpenerPolicy());
  app.use(helmet.crossOriginResourcePolicy({ policy: "same-site" }));
  app.use(helmet.dnsPrefetchControl({ allow: false }));
  app.use(helmet.frameguard({ action: 'deny' }));
  app.use(helmet.hidePoweredBy());
  app.use(helmet.hsts({
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }));
  app.use(helmet.ieNoOpen());
  app.use(helmet.noSniff());
  app.use(helmet.originAgentCluster());
  app.use(helmet.permittedCrossDomainPolicies({ permittedPolicies: 'none' }));
  app.use(helmet.referrerPolicy({
    policy: ['strict-origin-when-cross-origin']
  }));
  app.use(helmet.xssFilter());
}

module.exports = { configureSecurityHeaders };
```

## Success Indicators

You've mastered secure coding when you can:

- ✅ Identify and prevent OWASP Top 10 vulnerabilities
- ✅ Implement secure authentication and authorization
- ✅ Write parameterized queries consistently
- ✅ Properly validate and sanitize all inputs
- ✅ Use cryptography correctly (encryption, hashing, signing)
- ✅ Configure security headers and HTTPS
- ✅ Implement proper logging without exposing sensitive data
- ✅ Conduct security-focused code reviews
- ✅ Use security scanning tools effectively
- ✅ Stay updated on emerging security threats

## Related Skills

- [[Code Review]](../collaboration-skills/code_review.md) - Security-focused code reviews
- [[Debugging]](../behavior-skills/debugging.md) - Investigating security incidents
- [[System Architecture]](../designing-skills/system_architecture.md) - Secure system design
- [[DevOps & CI/CD]](../devops-skills/ci_cd.md) - Security in pipelines

---

*Version: 1.0.0 | Last Updated: 2024 | Next Review: Q2 2025*
