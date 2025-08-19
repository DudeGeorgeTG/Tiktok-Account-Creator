# TikTok Account Creator

A sophisticated Python implementation for automating TikTok account creation through their official API with proper request signing and encryption. This tool specifically targets the TikTok Creator platform (AID 1233) used by the main TikTok application.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Requests](https://img.shields.io/badge/Requests-Latest-green)
![Security](https://img.shields.io/badge/Security-XOR%20Encryption-yellow)

## ⚠️ CRITICAL REQUIREMENT: DEVICE IDENTIFICATION

**To avoid immediate account bans and detection, you MUST use real device identifiers:**

- **Device ID**: Unique hardware identifier (e.g., `7528525775047132680`)
- **Install ID**: Installation-specific identifier (e.g., `7528525992324908807`)
- **OpenUDID**: Device-specific unique identifier (e.g., `7a59d727a58ee91e`)
- **CDID**: Client device identifier (e.g., `a90f0ed5-8028-413e-a00d-77e931779d00`)

Using randomized or fake identifiers will result in immediate account suspension. This implementation specifically targets TikTok's Creator platform (AID 1233) which has enhanced security measures.

## ✨ Features

- **Official TikTok Creator API**: Targets AID 1233 (main TikTok application)
- **Real Device Emulation**: Uses authentic device parameters to avoid detection
- **Secure Communication**: Implements XOR encryption for sensitive data transmission
- **Request Signing**: Properly signs all API requests using TikTok's security protocol
- **Session Management**: Maintains consistent sessions across requests
- **Error Handling**: Comprehensive error handling with informative feedback
- **Account Storage**: Automatically saves successful accounts to files
- **Timestamp Rotation**: Dynamically updates timestamps to avoid detection

## 🛠️ Technical Implementation

This tool reverse-engineers TikTok's Android app API calls to create accounts programmatically. It handles the complete flow:

1. **Email Verification**: Sends verification code to the provided email
2. **Code Verification**: Validates the received code
3. **Account Creation**: Completes the registration process
4. **Session Extraction**: Retrieves and stores the session token

## 📦 Installation

```bash
git clone https://github.com/yourusername/tiktok-account-creator.git
cd tiktok-account-creator
pip install requests SignerPy
