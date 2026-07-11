\# 🌱 AgriInsight AI



> AI-Powered Smart Agriculture Assistant for Early Plant Disease Detection and Intelligent Farming Recommendations



!\[Python](https://img.shields.io/badge/Python-3.11-blue)

!\[FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)

!\[React](https://img.shields.io/badge/React-Frontend-61DAFB)

!\[TensorFlow](https://img.shields.io/badge/TensorFlow-AI-orange)

!\[License](https://img.shields.io/badge/License-MIT-red)



\---



\## 📖 Overview



Agriculture plays a vital role in the economy, yet many farmers struggle to identify plant diseases at an early stage. Delayed diagnosis often results in crop loss, excessive pesticide usage, and reduced productivity.



\*\*AgriInsight AI\*\* is an intelligent agriculture assistant that leverages Artificial Intelligence, Computer Vision, Explainable AI, Weather Forecasting, and Large Language Models to help farmers identify plant diseases and receive accurate treatment recommendations through a simple mobile/web interface.



The farmer only needs to upload an image of a plant leaf, and the system performs disease detection, severity analysis, treatment recommendation, weather verification, pesticide calculation, and report generation.



\---



\# 🎯 Problem Statement



Farmers often face challenges such as:



\- Difficulty identifying plant diseases.

\- Lack of access to agricultural experts.

\- Incorrect pesticide usage.

\- Crop damage due to delayed treatment.

\- Weather uncertainty before spraying pesticides.

\- Limited access to trusted agricultural guidance.



These issues increase farming costs and reduce crop yield.



\---



\# 💡 Proposed Solution



AgriInsight AI provides an AI-driven solution where farmers can simply upload a leaf image.



The application automatically:



\- Detects the disease.

\- Estimates confidence score.

\- Determines infection severity.

\- Explains why the disease occurred.

\- Suggests organic and chemical treatments.

\- Calculates pesticide dosage.

\- Checks weather conditions before spraying.

\- Finds nearby agricultural stores.

\- Generates downloadable PDF reports.

\- Provides an agriculture chatbot for additional guidance.



\---



\# 🚀 Key Features



\## 🌿 Disease Detection



\- Upload plant leaf image

\- AI-based disease prediction

\- Confidence percentage



\---



\## 📊 Severity Analysis



Classifies disease into:



\- Mild

\- Moderate

\- Severe



\---



\## 🔍 Explainable AI (Grad-CAM)



Highlights infected regions of the leaf to increase transparency and user trust.



\---



\## 💊 Treatment Recommendation



Provides:



\- Organic treatment

\- Chemical treatment

\- Recommended pesticides

\- Safety precautions



\---



\## 🌦 Weather Recommendation



Checks:



\- Rain forecast

\- Humidity

\- Temperature

\- Wind speed



Recommends whether pesticide spraying is suitable.



\---



\## 🧪 Pesticide Calculator



Calculates:



\- Required pesticide quantity

\- Water quantity

\- Tank refill count



Based on land area.



\---



\## 📍 Nearby Agricultural Resources



Locate nearby:



\- Fertilizer Shops

\- Seed Shops

\- Krishi Kendras



using Google Maps API.



\---



\## 🤖 AI Agriculture Chatbot



Supports:



\- English

\- Hindi

\- Marathi



Answers farming-related questions using trusted agricultural knowledge.



\---



\## 📑 PDF Report Generation



Generates detailed reports containing:



\- Disease name

\- Confidence score

\- Severity

\- Symptoms

\- Causes

\- Treatment

\- Weather recommendations

\- Pesticide calculation



\---



\## 📈 Scan History



Stores all previous disease reports for future reference.



\---



\# 🧠 AI Agent Architecture



The system is built using multiple intelligent AI agents.



| Agent | Responsibility |

|--------|---------------|

| Vision Agent | Detects disease from leaf image |

| Severity Agent | Calculates infection severity |

| Diagnosis Agent | Generates final diagnosis |

| Knowledge Agent | Retrieves trusted agricultural information |

| Explanation Agent | Explains disease in simple language |

| Treatment Agent | Suggests treatments |

| Weather Agent | Checks weather conditions |

| Resource Agent | Finds nearby agricultural resources |

| Report Agent | Generates PDF reports |

| Chatbot Agent | Answers farming questions |



\---



\# 🔄 Project Workflow



```

Farmer Uploads Leaf Image

&#x20;           │

&#x20;           ▼

Disease Detection Model

&#x20;           │

&#x20;           ▼

Severity Analysis

&#x20;           │

&#x20;           ▼

Explainable AI (Grad-CAM)

&#x20;           │

&#x20;           ▼

Knowledge Retrieval (RAG)

&#x20;           │

&#x20;           ▼

Treatment Recommendation

&#x20;           │

&#x20;     ┌─────┼───────────┐

&#x20;     ▼     ▼           ▼

Weather   Calculator   Nearby Shops

&#x20;     │

&#x20;     ▼

Generate PDF Report

&#x20;     │

&#x20;     ▼

Dashboard \& History

```



\---



\# 🏗 System Architecture



```

Frontend (React)

&#x20;       │

&#x20;       ▼

FastAPI Backend

&#x20;       │

&#x20;┌──────┼────────────┐

&#x20;▼      ▼            ▼

AI Model  Weather API  Google Maps API

&#x20;│

&#x20;▼

TensorFlow Model

&#x20;│

&#x20;▼

Disease Prediction

&#x20;│

&#x20;▼

Database

&#x20;│

&#x20;▼

PDF Report

```



\---



\# 🛠 Technology Stack



\## Frontend



\- React.js

\- Vite

\- Tailwind CSS

\- Framer Motion

\- React Router

\- Axios



\## Backend



\- Python

\- FastAPI

\- SQLAlchemy

\- Pydantic



\## Artificial Intelligence



\- TensorFlow

\- EfficientNetB0

\- OpenCV

\- Grad-CAM

\- NumPy



\## Generative AI



\- OpenAI GPT / Llama

\- RAG

\- FAISS



\## Database



\- SQLite

\- PostgreSQL (Future)



\## APIs



\- OpenWeather API

\- Google Maps API



\## PDF



\- ReportLab



\---



\# 📁 Project Structure



```

AgriInsight-AI

│

├── frontend

│

├── backend

│

├── ai\_model

│

├── agents

│

├── services

│

├── database

│

├── reports

│

├── assets

│

├── docs

│

├── README.md

│

├── requirements.txt

│

└── package.json

```



\---



\# ⚙ Installation



\## Clone Repository



```bash

git clone https://github.com/yourusername/AgriInsight-AI.git



cd AgriInsight-AI

```



\---



\## Backend



```bash

cd backend



pip install -r requirements.txt



uvicorn main:app --reload

```



\---



\## Frontend



```bash

cd frontend



npm install



npm run dev

```



\---



\# 📷 Screenshots



Add screenshots here.



\- Landing Page

\- Dashboard

\- Disease Detection

\- Treatment Recommendation

\- Weather

\- Chatbot

\- PDF Report



\---



\# 🔮 Future Enhancements



\- Drone-based crop monitoring

\- IoT sensor integration

\- Offline mobile application

\- Disease prediction before symptoms appear

\- Satellite crop analysis

\- Farmer community platform



\---



\# 👨‍💻 Team



\*\*Team Name:\*\* \*(Add your team name)\*



| Name | Role |

|------|------|

| Member 1 | AI/ML |

| Member 2 | Backend |

| Member 3 | Frontend |

| Member 4 | Documentation |



\---



\# 🏆 Hack4Humanity 2026



This project was developed as part of the \*\*Hack4Humanity 2026 Hackathon\*\*, aiming to empower farmers with AI-driven decision support for sustainable agriculture.



\---



\# 📄 License



This project is licensed under the MIT License.



\---



\# ⭐ Support



If you found this project useful, consider giving it a ⭐ on GitHub.



Together, let's make farming smarter with AI! 🌱

