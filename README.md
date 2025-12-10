# Cognitive Resonance Engine

An AI-powered audience research platform that transforms basic client information into comprehensive market intelligence using advanced LLM capabilities.

## Overview

The Cognitive Resonance Engine conducts deep-dive audience analysis by:
- Gathering company information via Perplexity Sonar Deep Research
- Generating comprehensive Ideal Customer Profiles (ICPs)
- Mapping Value Propositions using the VPC framework
- Building Pain Point Taxonomies using JTBD methodology
- Creating 4-stage Customer Journey Maps
- Exporting actionable reports in DOCX and Markdown formats

## Features

- **Multi-Model Support**: Choose from 6 LLM models via OpenRouter
  - `perplexity/sonar-deep-research` (Web research)
  - `anthropic/claude-sonnet-4.5`
  - `google/gemini-2.5-flash-preview-09-2025`
  - `openai/gpt-5-mini`
  - `openai/gpt-4.1`
  - `x-ai/grok-4.1-fast`

- **Comprehensive Research Pipeline**:
  1. Data Ingestion (company research)
  2. Audience Research (ICP generation)
  3. USP Extraction (Value Proposition Canvas)
  4. Pain Point Taxonomy (JTBD analysis)
  5. Customer Journey Mapping (4-stage maps)

- **Export Options**: DOCX and Markdown reports
- **Cost Tracking**: Token usage and cost estimation

## Installation

### Prerequisites
- Python 3.9+
- OpenRouter API key

### Setup

1. Clone or download the project:
```bash
cd "C:\Users\admin\Documents\Marketing\Roger SEO\Scripts\Cognitive Resonance Engine"
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure secrets for local development:
Create `.streamlit/secrets.toml`:
```toml
[api_keys]
OPENROUTER_API_KEY = "sk-or-v1-your-key-here"

[model_config]
default_analysis_model = "anthropic/claude-sonnet-4.5"
research_model = "perplexity/sonar-deep-research"
```

5. Run the application:
```bash
streamlit run app/main.py
```

## Streamlit Cloud Deployment

1. Push code to a GitHub repository
2. Connect to Streamlit Cloud
3. Add secrets in Streamlit Cloud dashboard:
   - Go to App Settings > Secrets
   - Add your `OPENROUTER_API_KEY`

## Project Structure

```
Cognitive Resonance Engine/
├── .streamlit/
│   └── secrets.toml          # API keys (local dev)
├── app/
│   ├── main.py               # Streamlit entry point
│   ├── config.py             # Configuration
│   ├── ui/                   # UI components
│   ├── core/                 # Business logic
│   ├── llm/                  # LLM integration
│   ├── export/               # Export functionality
│   ├── models/               # Data models
│   └── utils/                # Utilities
├── prompts/                  # Prompt templates
├── tests/                    # Unit tests
├── requirements.txt
├── README.md
└── ARCHITECTURE.md           # Detailed architecture docs
```

## Usage

1. **Enter Client Information**:
   - Company name and website URL
   - About page and Products/Services URLs
   - Industry and business model (B2B/B2C)
   - Any additional context

2. **Select Analysis Model**:
   - Choose your preferred LLM for analysis
   - Perplexity Sonar is always used for initial research

3. **Run Analysis**:
   - Click "Start Research" to begin the pipeline
   - Monitor progress through each stage

4. **Review Results**:
   - View generated ICPs, Value Propositions, Pain Points
   - Explore Customer Journey Maps

5. **Export Reports**:
   - Download DOCX or Markdown reports
   - View token usage and cost summary

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed technical documentation including:
- System architecture diagrams
- Module specifications
- Data flow documentation
- Prompt templates
- Output schemas

## Frameworks Used

The application implements several established frameworks:
- **Value Proposition Canvas (VPC)** - Strategyzer
- **Jobs-to-be-Done (JTBD)** - Clayton Christensen
- **Four Forces of Progress** - Bob Moesta
- **Customer Journey Mapping** - 4-stage model

## API Costs

Costs vary by model. The app includes a cost tracker that estimates:
- Input tokens used
- Output tokens generated
- Estimated cost per session

Typical research session: ~50,000-100,000 tokens total

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

Proprietary - Internal Use Only

## Support

For issues or questions, contact the development team.

---

*Built with Streamlit + OpenRouter*