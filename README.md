![Chile Banner](assets/chile_banner.jpg)

# Theory and Practice of Applied Predictive Groundwater Modeling
Materials and tutorials for the GMDSI Predictive Modeling Workshop in Santiago, 2025.

# Dates
8-9 September 2025, 9am-6pm

# Location
Club Providencia, Av. Pocuro 2878.
[View on Google Maps](https://maps.app.goo.gl/hDKMge5gjs2Khn8a9)

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6381.873477142874!2d-70.59469492251274!3d-33.43176557339686!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662cf0c1277e025%3A0xc5e46a0fa6fc5d0a!2sClub%20Providencia!5e1!3m2!1sen!2sau!4v1756443793910!5m2!1sen!2sau" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

## MCs
- Jeremy White
- Ed de Sousa
- Pablo Ortega
- Rodrigo Herrera

## Software
This workshop consists of jupyter notebooks that use pyemu and pestpp to run all the good stuff from uncertainty analysis to optimization managemnt. This repository is self contained, meaning that all dependencies are included here and you should not needed to install anything else. We encourage everyone to clone this repository and install the environment using:


Este taller está compuesto por Jupyter Notebooks que utilizan [PyEMU](https://github.com/pypest/pyemu) y [PEST++](https://github.com/usgs/pestpp) para realizar desde análisis de incertidumbre hasta optimización automatica (terrible de bkn).
El repositorio es selfcontained, lo que significa que todas las dependencias necesarias se encuentran incluidas y no será necesario instalar nada adicional (incluso tenemos los ejecutables de modflow). Se recomienda a todos los participantes clonar este repositorio e instalar el environment:

```bash
conda env create -f environment.yml

conda activate gmdsi_tut
```

## Schedule
### Day 1: Concepts, Theory and Experiences                                                         

| Time | Topic                                                                           | Lead(s)         |
|------|---------------------------------------------------------------------------------|-----------------|
| 9:00 | Overview and intros:                                                            | All             |
| 10:00| Intro to Uncertainty: Bayes and learning from data                              | JW              |
| 10:45| Coffee break                                                                    |                 |
| 11:00| Uncertainty in groundwater modelling: sources, importance, mitigation           | EdS             |
| 11:45| Heterogeneity: geostatistics, pilot points, uncertainty, parsimony fallacy      | PO              |
| 12:30| Lunch break                                                                     |                 |
| 13:30| Reducing uncertainty: inverse problems, GLM, ensemble methods, applied examples | JW, PO, CV      |
| 14:15| The value of data: data worth, ensemble variance, applied example               | EdS             |
| 15:00| Coffee break                                                                    |                 |
| 15:15| Management optimization & hydroeconomics                                        | JW, PO, EdS     |
| 16:15| Data-driven modeling & Emulation: theory and applied example                    | JW, PO          |

### Day 2: Hands-on Practice with Decision Support Modelling Software                                               

| Time  | Topic                                                                                                   | Lead(s)         |
|-------|---------------------------------------------------------------------------------------------------------|-----------------|
| 9:00  | Modeling discussion and IT support: problem decomposition, workflows, UA results, model types           | All             |
| 10:00 | GUIs and scripting: overview, workflow, automation, versioning, coder lifestyle                         | PO, JW          |
| 10:45 | Coffee break                                                                                            |                 |
| 11:00 | Introduce synthetic case & model: Freyberg history, model building                                      | JW              |
| 11:45 | PESTPP the hard way: control/template/instruction files, high-dim problems, hands-on                    | EdS, RH         |
| 12:30 | Lunch break                                                                                             |                 |
| 13:30 | How to run pestpp: command line, troubleshooting, parallelization, hands-on                             | EdS             |
| 14:15 | Live demo pyemu: PstFrom, pilot points, geostatistics, prior                                            | PO              |
| 15:00 | Coffee break                                                                                            |                 |
| 15:15 | History matching & UA with pestpp-ies: notebook, obs noise, parallel run, post-process, hands-on        | JW              |
| 16:00 | Optimization with pestpp-opt/pestpp-mou: decision variables, objectives, constraints                    | JW              |
| 16:45 | Set up your own emulator: obs setup, training, pypestworker                                             | PO              |
