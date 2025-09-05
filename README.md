![Chile Banner](assets/chile_banner.jpg)

# Theory and Practice of Applied Predictive Groundwater Modeling
Materials and tutorials for the GMDSI Predictive Modeling Workshop in Santiago, 2025.

# Dates
8-9 September 2025, 9am-6pm

# Location
Club Providencia, Av. Pocuro 2878.
[View on Google Maps](https://maps.app.goo.gl/hDKMge5gjs2Khn8a9)

## MCs
- Jeremy White
- Ed de Sousa
- Pablo Ortega
- Rodrigo Herrera


## Instrucciones de instalación

**Descarga el repositorio del curso:**

Puedes hacerlo de dos maneras:
 - (1) (más fácil) Descarga el repo como archivo zip desde aquí: [gmdsi-workshop-chile2025](https://github.com/p-ortega/gmdsi-workshop-chile2025). Descomprime la carpeta y trabaja desde ahí.
 - (2) (recomendado; requiere familiaridad con git). Instala git siguiendo las instrucciones aquí: [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Regístrate en GitHub y luego clona el repo [gmdsi-workshop-chile2025](https://github.com/p-ortega/gmdsi-workshop-chile2025).

**Instala Python y las dependencias:**
 - Si ya tienes Python instalado usando Anaconda, puedes saltarte este paso. Si no, instala [miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#download).
 - Si usas __Windows__: ve al menú inicio y abre "Anaconda prompt". Se abrirá una ventana de línea de comandos de anaconda. En __Linux__ o __MacOS__, simplemente usa la terminal estándar. Navega a la carpeta del repo del curso en tu máquina. Hazlo escribiendo "cd *tu ruta de carpeta*" y presionando < enter >. Reemplaza *tu ruta de carpeta* por la ruta donde tienes la carpeta del curso en tu compu.
 - Luego, escribe `mamba env create -f environment.yml` (o `conda env create -f environment.yml` si `mamba` no te funciona). Esto creará un entorno de anaconda llamado "gmdsitut" e instalará las dependencias de python necesarias para el curso. Puede tardar un rato. Si quieres, puedes revisar el archivo *environment.yml* en la carpeta del repo para ver qué dependencias se van a instalar.

**Inicia jupyter notebook**
Vas a tener que hacer este paso cada vez que quieras abrir uno de los notebooks del curso.
Para iniciar el jupyter notebook:
- Windows: abre el Anaconda prompt y escribe `conda activate gmdsitut`
- Mac/Linux: abre una terminal y escribe `conda activate gmdsitut`
- Luego navega a la carpeta donde descargaste el repo del curso y escribe `jupyter notebook`
Se debería iniciar una instancia de jupyter notebook dentro de la carpeta del repo. Usando el navegador, ahora puedes ir a la carpeta "tutorials", abrir uno ¡y ya estás listo!

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
