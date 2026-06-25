FROM rocker/r-ver:4.4.2

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        jags \
        libglpk-dev \
        libcurl4-openssl-dev \
    && mkdir -p /usr/lib/JAGS \
    && ln -sf /usr/lib/x86_64-linux-gnu/JAGS/modules-4 /usr/lib/JAGS/modules-4 \
    && rm -rf /var/lib/apt/lists/*

ENV RENV_CONFIG_REPOS_OVERRIDE=https://packagemanager.posit.co/cran/__linux__/noble/latest
ENV RENV_CONFIG_EXTERNAL_LIBRARIES=/usr/local/lib/R/site-library

RUN R -e "install.packages('renv', repos='https://cloud.r-project.org')"
RUN R -e "install.packages('distributional', repos='https://cran.r-project.org')"

WORKDIR /app

COPY renv.lock .
RUN R -e "renv::restore()"

COPY src/ .

ENTRYPOINT ["Rscript", "run.R"]
