# LicenseGuard - Project Brief

## Vision
The simplest way for indie developers to add license key protection to their desktop, mobile, or Electron apps.

## Problem Statement
Indie developers selling downloadable software need license key systems but:
- Rolling custom solutions is tedious and error-prone
- Enterprise solutions (Keygen, Cryptlex) are overpriced for small developers
- No simple, developer-friendly API exists at indie-friendly prices

## Target Users
- Solo developers selling desktop apps
- Indie game developers
- Electron app creators
- Mobile app developers with premium features
- Small software companies (<10 employees)

## Core Features (MVP)

### License Key Generation
- Generate unique, secure license keys
- Support multiple key formats (alphanumeric, UUID-based, custom patterns)
- Bulk generation for resellers
- Key metadata (customer email, purchase date, expiry)

### Validation API
- Simple REST API for key validation
- Offline validation support (signed keys)
- Rate limiting and abuse detection
- Machine/device fingerprinting (optional)

### Dashboard
- View all licenses
- Revoke/suspend keys
- Usage analytics
- Customer management

### Developer Experience
- SDKs for popular languages (Python, Node, Go, Rust, C#)
- Copy-paste code snippets
- Webhook notifications (new activation, suspicious activity)

## Non-Goals (v1)
- Subscription/recurring license management (v2)
- Feature flags (v2)
- White-label solution (v2)
- On-premise deployment (maybe never)

## Success Metrics
- 50 paying customers in 90 days
- $750 MRR target
- <2 support tickets per week
- 99.9% API uptime

## Competitive Landscape
| Competitor | Pricing | Weakness |
|------------|---------|----------|
| Keygen.sh | $99+/mo | Too expensive for indies |
| Cryptlex | $25+/mo | Complex, enterprise-focused |
| Gumroad | Built-in | Limited functionality |
| Custom | Free | Time-consuming, error-prone |

## Positioning
"License keys for indie developers. Simple API. Fair pricing. Ship in 10 minutes."

## Pricing Strategy
- **Free tier:** 100 validations/month (lead gen)
- **Starter:** $15/mo - 5,000 validations, 1 product
- **Pro:** $39/mo - Unlimited validations, 5 products, priority support
- **Usage-based:** $0.002 per validation (optional overage)
