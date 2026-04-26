# Dental Clinic Website (Flask)

A lightweight, data-driven single-page website for a dental clinic, built with Python and Flask. The website content (such as services, testimonials, clinic details, and images) is dynamically loaded from a `data.json` file, making it incredibly easy to update without having to modify the HTML template.

## Features
- **Dynamic Content**: Uses `data.json` for seamless content management.
- **Responsive Design**: An elegant, warm organic theme that works beautifully on mobile and desktop.
- **WhatsApp Integration**: Direct booking links and patient chat handled seamlessly via WhatsApp.
- **Dynamic Local Images**: Integrated routing for loading clinic branding and service images from the `static/` directory.
- **Interactive UI**: Includes a testimonial carousel and integrated Google Maps for direct routing.

## Prerequisites
- Python 3.7+
- git

## Startup Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/balakrishnasurya/dental_site_flask.git
   cd dental_site_flask
   ```

2. **Create and activate a virtual environment**:
   *   Windows (cmd/powershell):
       ```bash
       python -m venv venv
       .\venv\Scripts\activate
       ```
   *   macOS/Linux:
       ```bash
       python3 -m venv venv
       source venv/bin/activate
       ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

5. **View the site**:
   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000/).

## Customization
To update the website content, logo, services, contact information, or images, simply edit the `data.json` file and place any new local images in the `static/images/` directory.
