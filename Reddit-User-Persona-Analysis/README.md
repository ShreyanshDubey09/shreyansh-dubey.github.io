# 🤖 AI-Powered Reddit User Persona Generator

## 🎯 Project Overview
Advanced data analysis tool that leverages Reddit API and AI to generate comprehensive user personas for marketing and research purposes. This project demonstrates expertise in data scraping, natural language processing, and automated analysis workflows.

### 🚀 Business Impact
- **Automated user profiling** reduces manual analysis time from hours to minutes
- **Marketing teams** can identify target demographics instantly
- **Scalable solution** for social media intelligence and customer research

## 📊 Key Features
- ✅ **Automated Reddit Data Extraction** using PRAW API
- ✅ **AI-Powered Content Analysis** for personality trait identification  
- ✅ **Comprehensive User Profiling** including interests, writing style, profession
- ✅ **Source Citation** with links to original posts/comments
- ✅ **Batch Processing** capability for multiple users

## 🛠️ Technical Stack
- **Python 3.11** - Core programming language
- **PRAW** - Reddit API wrapper for data extraction
- **Natural Language Processing** - Text analysis and pattern recognition
- **Data Processing** - pandas, regex, datetime libraries
- **API Integration** - Reddit OAuth and rate limiting

## 📈 Sample Results
**Input:** Reddit user profile URL  
**Output:** Detailed persona including:
- 🎯 **Personality Traits** - Analytical, creative, detail-oriented
- 🧠 **Interests & Hobbies** - Technology, gaming, photography  
- 💬 **Communication Style** - Formal, technical, friendly
- 💼 **Profession Indicators** - Software developer, data analyst
- 📌 **Source Evidence** - Direct links to supporting posts

## 🔧 Setup & Installation

### Prerequisites
- Python 3.11+
- Reddit API credentials (free registration required)

### Installation Steps
Clone repository
git clone https://github.com/ShreyanshDubey09/Reddit-User-Persona-Analysis.git
cd Reddit-User-Persona-Analysis

Install dependencies
pip install -r requirements.txt

Configure Reddit API credentials
Edit main.py with your credentials from https://www.reddit.com/prefs/apps
text

### API Configuration
1. Visit [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Create new application (script type)
3. Copy credentials to main.py:
client_id = 'your_client_id'
client_secret = 'your_client_secret'
user_agent = 'script:reddit-persona:v1.0 (by u/your_username)'

text

## ▶️ Usage
python main.py

Enter Reddit profile URL when prompted
Example: https://www.reddit.com/user/username/
text

## 📁 Project Structure
Reddit-User-Persona-Analysis/
├── main.py # Core analysis script
├── requirements.txt # Python dependencies
├── output/ # Generated persona files
│ ├── username_raw.txt # Raw scraped data
│ └── username.txt # Analyzed persona
├── README.md # Project documentation
└── examples/ # Sample outputs

text

## 🎯 Skills Demonstrated
- **Data Extraction** - Reddit API integration and rate limiting
- **Text Processing** - Natural language analysis and pattern recognition
- **Automated Analysis** - Systematic approach to user profiling
- **API Management** - OAuth authentication and error handling
- **Data Pipeline** - End-to-end workflow from scraping to insights

## 📊 Business Applications
- **Marketing Research** - Identify target audience characteristics
- **Product Development** - Understand user needs and preferences  
- **Content Strategy** - Tailor messaging to audience communication styles
- **Competitive Analysis** - Analyze competitor customer base

## 🔮 Future Enhancements
- [ ] **Sentiment Analysis** integration
- [ ] **Multi-platform support** (Twitter, LinkedIn)
- [ ] **Dashboard visualization** with charts and graphs
- [ ] **Bulk processing** for multiple users
- [ ] **Machine Learning** classification models

## 🏆 Project Highlights
- **Real-world application** with immediate business value
- **Modern AI integration** showcasing current technology trends
- **Scalable architecture** designed for production deployment
- **Comprehensive documentation** for easy reproduction and extension

## 📞 Contact
**Shreyansh Dubey** - Data Analyst  
📧 [sdubey0009999@gmail.com](mailto:sdubey0009999@gmail.com)  
💼 [Portfolio](https://shreyanshdubey09.github.io)  
📱 +91 7222849267

---
*This project demonstrates advanced data analysis capabilities combining API integration, natural language processing, and automated insight generation - key skills for modern data analyst roles.*