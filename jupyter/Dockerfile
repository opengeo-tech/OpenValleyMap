# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/minimal-notebook
ARG NB_UID=1000

USER root

# RUN apt update && \
#     apt install -y --no-install-recommends git
    #gcc libgeos-dev && \
#     rm -rf /var/lib/apt/lists/*
# #deps for cartopy https://scitools.org.uk/cartopy/docs/latest/installing.html#requirements

USER $NB_UID

# RUN git clone https://github.com/SciTools/cartopy.git \
# 	&& cd cartopy \
# 	&& conda env create -f environment.yml \
# 	&& conda activate cartopy-dev \
# 	&& pip install -e .

RUN fix-permissions /home/$NB_USER

RUN pip install ipywidgets \
	#cartopy \
	matplotlib \
	pandas \
	numpy \
	folium \
	descartes \
	geopandas \
	rasterio
	# \ pyflwdir

RUN conda install pyflwdir -c conda-forge

# RUN pip install
# RUN pip install
# RUN pip install

#COPY povo.ipynb .
#COPY povo.geojson .

#TODO CMD ["echo","STARTED JUPYTER at http://localhost:8888/"]
