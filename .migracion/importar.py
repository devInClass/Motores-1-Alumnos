import json
import os
from pathlib import Path
import subprocess
import tempfile

workspace = Path(os.environ['GITHUB_WORKSPACE']).resolve()
plan = json.loads((workspace / '.migracion/plan.json').read_text(encoding='utf-8'))


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()


with tempfile.TemporaryDirectory(prefix='replica-curso-', dir=os.environ['RUNNER_TEMP']) as temporal:
    importado = Path(temporal) / 'repositorio'
    subprocess.run(['git', 'clone', str(workspace / '.migracion/historial.bundle'), str(importado)], check=True)
    assert git(importado, 'rev-parse', 'HEAD') == plan['origen_head']
    git(importado, 'config', 'user.name', 'devInClass')
    git(importado, 'config', 'user.email', '353121746+devInClass@users.noreply.github.com')
    for relativa, texto in plan['archivos'].items():
        destino = (importado / relativa).resolve()
        assert destino.is_relative_to(importado) and '.git' not in destino.relative_to(importado).parts
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(texto.encode('utf-8'))
    git(importado, 'add', '-A')
    assert git(importado, 'write-tree') == plan['arbol_esperado']
    git(importado, 'commit', '-m', 'Actualizar direcciones del curso a devInClass')
    git(importado, 'fetch', str(workspace), os.environ['GITHUB_SHA'])
    git(importado, 'merge', '--allow-unrelated-histories', '--strategy=ours', '--no-edit', 'FETCH_HEAD')
    assert git(importado, 'rev-parse', 'HEAD^{tree}') == plan['arbol_esperado']
    git(importado, 'merge-base', '--is-ancestor', plan['origen_head'], 'HEAD')
    git(workspace, 'fetch', str(importado), 'HEAD')
    git(workspace, 'merge', '--ff-only', 'FETCH_HEAD')
    git(workspace, 'push', 'origin', 'HEAD:main')
    print('Historial importado con árbol verificado', plan['arbol_esperado'])
