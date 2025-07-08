"""
from pathlib import Path

project_structure = {
    ".github": {
        "workflows": {
            "ci-cd.yaml": None,
            "tests.yaml": None,
            "release.yaml": None
        }
    },
    "configs": {
        "development.yaml": None,
        "production.yaml": None,
        "testing.yaml": None
    },
    "docs": {
        "architecture.md": None,
        "api-spec.yaml": None,
        "agent-specs.md": None
    },
    "src": {
        "agents": {
            "base.py": None,
            "style_analysis": {
                "__init__.py": None,
                "agent.py": None,
                "models.py": None
            },
            "transformation_planner": {
                "__init__.py": None,
                "agent.py": None,
                "models.py": None
            },
            # Add more agents here if needed
        },
        "api": {
            "endpoints": {
                "__init__.py": None,
                "transformation.py": None,
                "health.py": None
            },
            "middleware": {
                "auth.py": None,
                "logging.py": None
            },
            "server.py": None
        },
        "core": {
            "exceptions.py": None,
            "logging.py": None,
            "utils.py": None
        },
        "llm": {
            "clients": {
                "openai.py": None,
                "anthropic.py": None
            },
            "prompt_templates": {
                "style_analysis": {},
                "transformation": {}
            },
            "models.py": None
        },
        "models": {
            "agent.py": None,
            "workflow.py": None,
            "transformation.py": None
        },
        "monitoring": {
            "metrics.py": None,
            "tracing.py": None,
            "logging.py": None
        },
        "rag": {
            "retrievers": {
                "style_guide.py": None,
                "fact_checker.py": None
            },
            "vector_db": {
                "chroma.py": None,
                "pinecone.py": None
            },
            "models.py": None
        },
        "services": {
            "transformation.py": None,
            "quality_check.py": None
        },
        "tasks": {
            "queues.py": None,
            "workers.py": None
        },
        "workflow": {
            "builder.py": None,
            "manager.py": None,
            "models.py": None
        }
    },
    "tests": {
        "unit": {
            "agents": {},
            "services": {}
        },
        "integration": {
            "api": {},
            "workflow": {}
        },
        "e2e": {}
    },
    ".env.example": None,
    "Makefile": None,
    "pyproject.toml": None,
    "requirements.txt": None,
    "requirements-dev.txt": None,
    "README.md": None
}


def create_structure(base_path: Path, structure: dict):
  # Recursively create directory structure and files.
    for name, content in structure.items():
        path = base_path / name
        if content is None:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)
            print(f"Created file: {path}")
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {path}")
            create_structure(path, content)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    print(f"Creating project structure in: {root}")
    create_structure(root, project_structure)
"""

# New structure:


from pathlib import Path

project_structure = {
    "app": {
        "__init__.py": None,
        "main.py": None,
        "api": {
            "__init__.py": None,
            "endpoints.py": None
        },
        "agents": {
            "__init__.py": None,
            "style_analysis.py": None,
            "transformation_planning.py": None,
            "content_conversion.py": None,
            "quality_control.py": None,
            "workflow.py": None
        },
        "rag": {
            "__init__.py": None,
            "knowledge_base.py": None,
            "retriever.py": None
        },
        "models": {
            "__init__.py": None,
            "schemas.py": None
        },
        "utils": {
            "__init__.py": None,
            "config.py": None,
            "llm.py": None
        },
        "tests": {
            "__init__.py": None,
            "test_endpoints.py": None,
            "test_agents.py": None
        }
    },
    "data": {
        "style_guides.json": None,
        "transformation_examples.json": None
    },
    "requirements.txt": None,
    "README.md": None,
    "docker-compose.yml": None,
    ".env": None
}

def create_structure(base_path: Path, structure: dict):
    """Recursively create directory structure and files."""
    for name, content in structure.items():
        path = base_path / name
        if content is None:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)
            print(f"Created file: {path}")
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {path}")
            create_structure(path, content)

if __name__ == "__main__":
    root = Path(__file__).resolve().parent 
    root.mkdir(parents=True, exist_ok=True)
    print(f"Creating project structure in: {root}")
    create_structure(root, project_structure)
