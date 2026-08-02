# Runnable Projects: Learn by Building! 🚀

**Theory is good. Building is better.** Each project is a complete, minimal implementation you can run immediately.

---

## 📋 Available Projects

| Project | Guide | Lines | Time | Difficulty | Colab Ready |
|---------|-------|-------|------|------------|-------------|
| [RAG Chatbot](./rag-chatbot/) | [RAG](../guides/RAG/) | ~150 | 30 min | ⭐⭐ Beginner | ✅ Yes |

**More coming soon!** Each major guide will have a companion project.

---

## 🎯 How to Use These Projects

### For Complete Beginners:

1. **Complete prerequisites** - [Terminal](../prerequisites/terminal_basics.md), [Python](../prerequisites/python_basics.md), [Git](../prerequisites/git_basics.md)
2. **Read the guide chapter** - Understand the theory first
3. **Run the project** - Follow the README instructions
4. **Modify and experiment** - Change parameters, add features
5. **Build your own version** - Apply what you learned

### For Experienced Developers:

1. **Skim the code** - Get the architecture overview
2. **Run it** - Verify it works
3. **Optimize** - Improve performance or quality
4. **Extend** - Add new features
5. **Deploy** - Put it in production

---

## 💻 Running Projects

### Option A: Google Colab (Recommended)

Every project includes a Colab notebook with:
- ✅ Free GPU access
- ✅ Pre-installed dependencies
- ✅ Step-by-step execution
- ✅ No setup required!

Just click the "Open in Colab" badge in each project's README.

### Option B: Local Setup

```bash
# 1. Navigate to project
cd projects/project-name

# 2. Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the project
python main.py
# or
jupyter notebook notebook.ipynb
```

---

## 🎓 Learning Philosophy

### Why Projects Matter

Reading about AI ≠ Building AI

| Learning Method | Retention | Practical Skill |
|----------------|-----------|-----------------|
| Reading only | 10% | Low |
| Reading + Code examples | 30% | Medium |
| **Reading + Building projects** | **70%** | **High** |
| Teaching others | 90% | Expert |

### The Build-to-Learn Cycle

```
Read Theory → Run Project → Break It → Fix It → Modify It → Build Your Own
     ↓            ↓           ↓          ↓          ↓            ↓
  Concept    See it work  Learn from   Debugging  Customize   Mastery!
                                 mistakes      skills
```

---

## 🛠️ Project Standards

Every project follows these standards:

### Code Quality
- ✅ Under 300 lines (focused, not overwhelming)
- ✅ Heavily commented (every function explained)
- ✅ Clean structure (easy to follow)
- ✅ Error handling (graceful failures)

### Documentation
- ✅ Clear README (what, why, how)
- ✅ Requirements.txt (exact dependencies)
- ✅ Quick start guide (run in 5 minutes)
- ✅ Troubleshooting section (common errors)

### Accessibility
- ✅ Works on free Colab tier
- ✅ Minimal hardware requirements
- ✅ No paid APIs needed
- ✅ Beginner-friendly error messages

---

## 📊 Hardware Reality Check

All projects are designed to run on:

| Hardware Tier | What You Can Do | Cost |
|---------------|-----------------|------|
| **Google Colab Free** | All beginner projects | $0 |
| **Colab Pro** | Faster training, larger models | $10/mo |
| **Local Laptop (8GB RAM)** | CPU inference, small models | $0 (if you have laptop) |
| **Gaming PC (RTX 3060+)** | Full training, medium models | $800+ |

**Pro tip:** Start with free Colab. Only invest in hardware once you're committed!

---

## 🔗 Integration with Guides

Each project links directly to guide chapters:

```
Project Component → Guide Chapter
─────────────────────────────────────
Document Loading → RAG Ch.2: Data Preparation
Embeddings → RAG Ch.3: Training Retrievers  
Vector Store → RAG Ch.4: Building RAG Systems
LLM Integration → RAG Ch.5: Training Generators
```

**Study strategy:**
1. Read guide chapter
2. Run corresponding project section
3. Experiment with parameters
4. Return to next chapter

---

## 🐛 Getting Help

### If a Project Doesn't Work:

1. **Check the error** - Copy the exact message
2. **Visit [Common Errors](../errors/)** - 90% of issues are documented
3. **Check versions** - Make sure dependencies match
4. **Try Colab** - Rules out local setup issues
5. **Open an issue** - GitHub Issues for this repo

### Common Problems:

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| Import errors | Wrong environment | `pip install -r requirements.txt` |
| CUDA OOM | GPU memory full | Reduce batch size, use CPU |
| Slow performance | No GPU | Enable GPU in Colab |
| Bad results | Wrong model | Use recommended models |

---

## 🙏 Contributing Projects

Want to add a project? We'd love it!

### Contribution Guidelines:

1. **Pick a guide** - Must complement an existing guide
2. **Keep it minimal** - Under 300 lines
3. **Comment heavily** - Assume beginner reader
4. **Test on Colab** - Must work on free tier
5. **Write great docs** - README, requirements, troubleshooting
6. **Add examples** - Sample input/output

### Project Template:

```
projects/your-project/
├── README.md           # Complete instructions
├── requirements.txt    # Dependencies
├── main.py            # Main code file
├── notebook.ipynb     # Jupyter version
├── sample_data/       # Example data
└── tests/             # Basic tests (optional)
```

Submit via Pull Request with:
- [ ] Code complete and tested
- [ ] README with quick start
- [ ] Works on Colab free tier
- [ ] Links to relevant guide chapters

---

## 📈 Progression Path

Projects increase in complexity:

```
Beginner (⭐)
├── RAG Chatbot - Your first AI system
│
Intermediate (⭐⭐)
├── Image Classifier - CNN basics
├── Text Generator - Transformer fine-tuning
│
Advanced (⭐⭐⭐)
├── Multi-Agent System - Agentic workflows
├── Production Pipeline - MLOps deployment
```

---

## 🎁 Bonus Resources

### Learning Checklist

For each project:
- [ ] Read the associated guide chapter
- [ ] Run the project successfully
- [ ] Explain each function to someone (or rubber duck!)
- [ ] Modify at least one parameter
- [ ] Break something and fix it
- [ ] Build a mini-project using the same concepts

### Portfolio Building

These projects are portfolio-ready! Enhance them by:
1. Adding a nice UI (Gradio/Streamlit)
2. Deploying online (Hugging Face Spaces)
3. Writing a blog post about what you learned
4. Adding tests and CI/CD
5. Creating a demo video

---

<div align="center">

**Ready to build? Start with the [RAG Chatbot](./rag-chatbot/)!** 🤖

[← Back to Guides](../guides/) | [Prerequisites](../prerequisites/) | [Common Errors](../errors/)

</div>
