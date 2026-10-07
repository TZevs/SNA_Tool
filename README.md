# Social Network Analysis Tool For Businesses
An accessible social network / influence analysis tool that helps non-technical business users understand the structure of a network and their influence within it.
<br>

<img width="360" height="161" alt="UI_1" src="https://github.com/user-attachments/assets/3fe90ee6-dcd5-4add-8e63-2c7764922044" />
<img width="360" height="161" alt="UI_4" src="https://github.com/user-attachments/assets/dc9c8605-14f8-4a7e-8b48-cdc262d30e83" />
<img width="360" height="161" alt="UI_2" src="https://github.com/user-attachments/assets/dd38262a-5821-4f0d-b7c5-7ff3a5f8ba0b" />
<img width="360" height="161" alt="UI_5" src="https://github.com/user-attachments/assets/76da8109-8f46-4055-8111-1649bc89874a" />
<img width="360" height="161" alt="UI_3" src="https://github.com/user-attachments/assets/7c8441c1-20d1-4b0e-8fba-0df08ef14bd3" />


## 🎓 About This Project
> This is my final-year **dissertation** project for Software Engineering at Sheffield Hallam University (2026). It was developed to meet a marking criteria, so it is **not at a production-level standard**. 

🫟**Problem:** Social network analysis (SNA) can show importance within a network, however the available tools are more for academic purposes, not for practical applications that business users may be interested in. This tool takes an edge list and turns its analysis into clear interpretable roles with recommendations displayed on an interactive dashboard. 

🚪**Approach:** It is built as a modular pipeline (graph, global metrics, community, roles, recommendation, evaluation), with a FastAPI backend serving the results to a Dash frontend. Roles are assigned using percentile-based thresholds on the computed metrics, and validated with Spearman and Kendall rank correlation. 

🚦**Status:** Currently debugging, small data loading issue. High Fidelity Prototype. Tested on a medium sized network (the Facebook SNAP dataset), other datasets and larger networks are not reliably supported. 

### ✨ Features
- Loads and cleans an edge-list dataset then models it as a graph. 
- Computes Global Metrics: degree, eigenvector, betweenness, closeness, k-core, k-truss.
- Louvain Community Detection, with local metrics: z-score and participation coefficient. 
- Global and local role assignment based on percentile thresholds computed on the metrics.
- Role-based recommendations written for business users.
  - Global: Hub, Broker, Core, Spreader, Peripheral.
  - Local: Provincial Hub, Connector Hub, Kinless Hub, Peripheral, Ultra-Peripheral, Connector, Kinless.  
- Evaluation metrics: Spearman and Kendall correlation and modularity for community quality.
- Interactive dashboard UI with role distributions, community graphs, and metric charts. 

---
### 🛠️ Tech Stack
![Python](https://img.shields.io/badge/python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54)
<br>
![FastAPI](https://img.shields.io/badge/fastapi-%23009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![Dash](https://img.shields.io/badge/dash-%23008DE4.svg?style=for-the-badge&logo=dash&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)
<br>
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/plotly-%237A76FF.svg?style=for-the-badge&logo=plotly&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![: NetworkX](https://img.shields.io/badge/-NetworkX-informational?style=flat-square)
<br>
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-%23000000.svg?style=for-the-badge&logo=pycharm&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)

---
## 🚀 Run Locally
#### Installation
```bash
git clone https://github.com/TZevs/SNA_Tool.git
cd SNA_Tool
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
> _If using Windows here's a link for venv setup. [Python Venv](https://www.w3schools.com/python/python_virtualenv.asp)_
#### Usage
##### To run the pipeline:
> _If in PyCharm just open `pipeline.py`, click ▶️ button._
```bash
cd src/pipelines
python pipeline.py
```
##### To Run the Tool (separate terminals):
```bash
fastapi dev     # Run in Root directory
python frontend/dash_app/app.py 
```
Open the Dash app by following the local host link returned in the terminal. 

---
## 🔍 Known Issues & Improvements to be Made 
- Running the pipeline(currently run it via `python pipeline.py`: optimise speed with async, allow it to be ran when called. 
- NetworkX is slow on large networks: optimise the pipeline or try a faster library (igraph, graph-tool).
- Only the Facebook SNAP dataset is reliably supported: test and support more datasets.
- Static, unweighted networks only: adjust algorithms to support weighted and directed networks.

---
## 🤝 Credits 
This project was created as a final dissertation project for my degree at Sheffield Hallam University.<br>
Supervisor: Jaya Tangirala

Guimerà, R., & Nunes Amaral, L. A. (2005). Functional cartography of complex metabolic networks. Nature, 433(7028), 895–900. https://doi.org/10.1038/nature03288

Leskovec, J. (2026). Stanford Large Network Dataset Collection. Stanford.Edu. https://snap.stanford.edu/data/

## 📄 License
This project is licensed under the MIT License. 
