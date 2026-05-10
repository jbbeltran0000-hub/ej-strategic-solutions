# Environmental Justice Strategic Solutions Portal

A Streamlit web application showcasing compliance-ready pilot programs and proposals designed for non-profits, for-profits, and government agencies.

## 🚀 Quick Start - Deploy to Streamlit Cloud

### Prerequisites
- GitHub account (already connected)
- Streamlit Cloud account (free at https://share.streamlit.io)

### Deployment Steps

1. **Sign in to Streamlit Cloud**
   - Visit https://share.streamlit.io
   - Sign in with your GitHub account

2. **Create New App**
   - Click "New app"
   - Select:
     - Repository: `jbbeltran0000-hub/ej-strategic-solutions`
     - Branch: `main`
     - Main file path: `app.py`
   - Click "Deploy"

3. **Your app will be live in 2-3 minutes!**
   - URL: `https://share.streamlit.io/jbbeltran0000-hub/ej-strategic-solutions`

## ⚠️ Important Setup

Before your app goes live, **update the contact form email**:

1. Edit `app.py`
2. Find the line: `<form action="https://formsubmit.co/YOUR_EMAIL_HERE" method="POST">`
3. Replace `YOUR_EMAIL_HERE` with your actual email address
4. Commit and push the change
5. Streamlit will auto-redeploy within seconds

## 📋 Features

- **Government & Regulatory Compliance** - Air Quality Monitoring Pilot
- **Community Health & Advocacy** - Brain Justice & Neuro-Protection Initiative
- **Contact Form** - Partner inquiry submissions
- **Custom Branding** - Green theme (#2e7d32) for Environmental Justice focus

## 🛠️ Local Development

To run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Your app will be available at `http://localhost:8501`

## 📁 Project Structure

```
ej-strategic-solutions/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/config.toml # Streamlit configuration
└── README.md             # This file
```

## 🔧 Customization

- **Colors**: Edit `primaryColor` in `.streamlit/config.toml`
- **Content**: Update text in `app.py`
- **Projects**: Add new expanders in the PROJECT CATEGORIES section
- **Files**: Place PDFs/documents in the repo and reference them in `app.py`

## 📝 License

This project is designed for Environmental Justice initiatives.

---

**Need help?** Check the [Streamlit Documentation](https://docs.streamlit.io) or [GitHub Issues](https://github.com/jbbeltran0000-hub/ej-strategic-solutions/issues)