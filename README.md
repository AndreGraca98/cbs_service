# PDM Help

## Add git repos

```bash
pdm add "git+ssh://git@git.eu.clara.net/billing-system/orm.git@dev#egg=claranet-billing-orm"
```

## Manage a monorepo

<https://pdm-project.org/latest/usage/advanced/#use-pdm-to-manage-a-monorepo>

## Build docker example

```dockerfile
# build stage
FROM python:3.11-slim-bookworm as builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock README.md /project/
COPY src/ /project/src

# install dependencies and project into the local packages directory
WORKDIR /project
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


# run stage
FROM python:3.11-slim-bookworm

# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.11/lib /project/pkgs

# retrieve executables
COPY --from=builder /project/__pypackages__/3.11/bin/* /bin/

# set command/entrypoint, adapt to fit your needs
CMD ["python", "-m", "project"]
``````
