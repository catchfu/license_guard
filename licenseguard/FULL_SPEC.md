# LicenseGuard - Complete Product Specification

**Date:** 2026-02-09
**Status:** Ready for Build

---

## 1. Vision

The simplest way for indie developers to add license key protection to their desktop, mobile, or Electron apps.

**Tagline:** "License keys for indie developers. Ship in 10 minutes."

---

## 2. Problem Statement

Indie developers selling downloadable software need license key systems but:
- Rolling custom solutions is tedious and error-prone
- Enterprise solutions (Keygen, Cryptlex) are overpriced for small developers
- No simple, developer-friendly API exists at indie-friendly prices

---

## 3. Target Users

| Segment | Description | Pain Level |
|---------|-------------|------------|
| Solo developers | Selling desktop apps on Gumroad/own site | High |
| Indie game developers | Premium games with anti-piracy needs | Medium |
| Electron app creators | Cross-platform desktop apps | High |
| Mobile developers | Premium features unlocked by license | Medium |
| Small software companies | <10 employees, don't want to build in-house | Medium |

---

## 4. Core Features (MVP)

### 4.1 License Key Generation
- Generate unique, secure license keys
- Support multiple key formats:
  - Alphanumeric (XXXX-XXXX-XXXX-XXXX)
  - UUID-based
  - Custom patterns
- Bulk generation for resellers
- Key metadata:
  - Customer email
  - Purchase date
  - Expiry date (optional)
  - Max activations
  - Custom fields

### 4.2 Validation API
- Simple REST API for key validation
- Response includes:
  - Valid/invalid status
  - License metadata
  - Remaining activations
- Offline validation support (signed keys)
- Rate limiting and abuse detection
- Machine/device fingerprinting (optional)

### 4.3 Dashboard
- View all products
- View all licenses (filterable)
- Generate new licenses
- Revoke/suspend keys
- Usage analytics:
  - Validations over time
  - Geographic distribution
  - Abuse attempts
- Customer management

### 4.4 Developer Experience
- SDKs for popular languages:
  - Python
  - Node.js
  - Go
  - Rust
  - C#/.NET
- Copy-paste code snippets
- Webhook notifications:
  - New activation
  - Suspicious activity
  - License revoked

---

## 5. Non-Goals (v1)

| Feature | Reason | Target Version |
|---------|--------|----------------|
| Subscription/recurring licenses | Complexity | v2 |
| Feature flags | Scope creep | v2 |
| White-label solution | B2B complexity | v2+ |
| On-premise deployment | Support burden | Maybe never |
| Advanced analytics | Nice-to-have | v2 |

---

## 6. Technical Architecture

### 6.1 Recommended Stack
| Component | Technology | Reason |
|-----------|------------|--------|
| API | Go or Rust | Fast, low memory, cheap to run |
| Database | PostgreSQL (Neon/Supabase) | Reliable, familiar |
| Cache | Redis (Upstash) | Rate limiting, sessions |
| Hosting | Fly.io or Railway | Simple, auto-scaling |
| Auth | Clerk | No auth code to maintain |
| Payments | Stripe | Industry standard |
| Email | Resend | Developer-friendly |

### 6.2 API Endpoints (Draft)
```
POST   /api/v1/products              # Create product
GET    /api/v1/products              # List products
GET    /api/v1/products/:id          # Get product

POST   /api/v1/licenses              # Create license
GET    /api/v1/licenses              # List licenses
GET    /api/v1/licenses/:key         # Get license
PATCH  /api/v1/licenses/:key         # Update license
DELETE /api/v1/licenses/:key         # Revoke license

POST   /api/v1/validate              # Validate license key
POST   /api/v1/activate              # Activate license
POST   /api/v1/deactivate            # Deactivate license

GET    /api/v1/analytics             # Usage analytics
```

### 6.3 Database Schema (Draft)
```sql
-- Users (managed by Clerk)

-- Products
CREATE TABLE products (
  id UUID PRIMARY KEY,
  user_id TEXT NOT NULL,
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Licenses
CREATE TABLE licenses (
  id UUID PRIMARY KEY,
  product_id UUID REFERENCES products(id),
  license_key TEXT UNIQUE NOT NULL,
  customer_email TEXT,
  customer_name TEXT,
  max_activations INT DEFAULT 1,
  current_activations INT DEFAULT 0,
  expires_at TIMESTAMP,
  revoked BOOLEAN DEFAULT FALSE,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Activations
CREATE TABLE activations (
  id UUID PRIMARY KEY,
  license_id UUID REFERENCES licenses(id),
  machine_id TEXT NOT NULL,
  ip_address TEXT,
  user_agent TEXT,
  activated_at TIMESTAMP DEFAULT NOW(),
  deactivated_at TIMESTAMP
);

-- Validation logs (for analytics)
CREATE TABLE validation_logs (
  id UUID PRIMARY KEY,
  license_id UUID REFERENCES licenses(id),
  success BOOLEAN,
  ip_address TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 6.4 Infrastructure Costs (Estimated)
| Service | Cost/Month |
|---------|------------|
| Fly.io (API hosting) | $5-10 |
| Neon (Postgres) | $0-19 |
| Upstash (Redis) | $0-10 |
| Clerk (Auth) | $0-25 |
| Total | **$5-64** |

---

## 7. Pricing Strategy

### 7.1 Tiers
| Tier | Price | Validations | Products | Features |
|------|-------|-------------|----------|----------|
| Free | $0 | 100/mo | 1 | Basic validation |
| Starter | $15/mo | 5,000/mo | 1 | + Webhooks, SDKs |
| Pro | $39/mo | Unlimited | 5 | + Priority support, Analytics |

### 7.2 Overage (Optional)
- $0.002 per validation over limit

### 7.3 Competitive Positioning
| Competitor | Starting Price | Our Advantage |
|------------|---------------|---------------|
| Keygen.sh | $99/mo | 85% cheaper |
| Cryptlex | $25/mo | 40% cheaper, simpler |
| DIY | "Free" | Saves 20+ hours dev time |

---

## 8. Go-to-Market Strategy

### 8.1 Launch Channels
| Channel | Action | Timing |
|---------|--------|--------|
| Hacker News | Show HN post | Week 1 |
| Product Hunt | Launch day | Week 2 |
| Indie Hackers | Community post | Week 2 |
| Twitter/X | Thread + ongoing | Ongoing |
| Reddit | r/SideProject, r/gamedev | Week 1-2 |

### 8.2 SEO Keywords
- "license key api"
- "software license management"
- "electron app license"
- "desktop app license key"
- "indie developer licensing"

### 8.3 Content Strategy
- Quick start guide (SEO)
- "How to add licensing to your Electron app" (tutorial)
- "Why I built LicenseGuard" (story)
- SDK documentation (long-tail SEO)

---

## 9. Success Metrics

| Metric | 30-Day Target | 90-Day Target |
|--------|---------------|---------------|
| Signups | 100 | 300 |
| Paying customers | 15 | 50 |
| MRR | $225 | $750 |
| Churn | <5% | <5% |
| Support tickets/week | <3 | <5 |
| API uptime | 99.9% | 99.9% |

---

## 10. Timeline

| Week | Milestone |
|------|-----------|
| 1 | Architecture + API design complete |
| 2 | Core API (CRUD, validation) working |
| 3 | Dashboard MVP + Auth |
| 4 | SDKs (Python, Node) + Docs |
| 5 | Beta launch (HN, IH) |
| 6 | Product Hunt launch |
| 7-12 | Iterate based on feedback |

---

## 11. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Small TAM | Medium | High | Focus SEO, niche down to Electron |
| Security breach | Low | Critical | Audit code, use proven crypto |
| Big player enters | Low | Medium | Move fast, build community |
| High support load | Medium | Medium | Great docs, self-service |

---

## 12. Team

| Role | Agent | Responsibilities |
|------|-------|-----------------|
| Product Lead | PM + BA | Requirements, priorities |
| UX & Content Lead | UX + Tech Writer | Design, docs |
| Engineering Lead | Dev + Architect | Build it |
| QA Engineer | QA | Test it |
| Growth Lead | Marketing + Sales | Sell it |

---

## Appendix: Agent Prompts Location

All agent prompts stored in:
```
C:\QQ\Projects\agent_teams\licenseguard\agents\
```

Run sessions with:
```bash
python run_licenseguard_team.py <phase>
```

Phases: `discovery`, `design`, `build`, `launch`, `full`
