#!/usr/bin/env python3
"""
Script de comparação exaustiva: outputs/ vs HEMODOCTOR_CONSOLIDADO_v2.0_20251010/

Verifica:
1. Quais arquivos de outputs/ foram copiados para CONSOLIDADO
2. Quais arquivos NÃO foram copiados
3. Diferenças de conteúdo (MD5 checksums)
4. Mapeamento de localização
"""

import os
import hashlib
from pathlib import Path
from collections import defaultdict

# Diretórios
OUTPUTS_DIR = Path("/Users/abelcosta/Documents/HemoDoctor/docs/outputs")
CONSOLIDADO_DIR = Path("/Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010")

# Extensões relevantes
EXTENSIONS = {".md", ".csv", ".R", ".py", ".html", ".sh"}

# Pastas a ignorar
IGNORE_DIRS = {"venv", ".pytest_cache", "__pycache__", "node_modules"}


def calculate_md5(filepath):
    """Calcula MD5 checksum de um arquivo."""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return f"ERROR: {e}"


def get_files_in_dir(base_dir, ignore_dirs=None):
    """
    Retorna dicionário: {filename: [full_path1, full_path2, ...]}
    Para detectar arquivos duplicados.
    """
    if ignore_dirs is None:
        ignore_dirs = set()

    files_dict = defaultdict(list)

    for root, dirs, files in os.walk(base_dir):
        # Remove pastas ignoradas
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            filepath = Path(root) / file
            if filepath.suffix in EXTENSIONS:
                files_dict[file].append(filepath)

    return files_dict


def compare_directories():
    """Comparação principal."""

    print("=" * 80)
    print("COMPARAÇÃO EXAUSTIVA: outputs/ vs HEMODOCTOR_CONSOLIDADO_v2.0_20251010/")
    print("=" * 80)
    print()

    # 1. Listar arquivos em outputs/
    print("1. Listando arquivos em outputs/...")
    outputs_files = get_files_in_dir(OUTPUTS_DIR, IGNORE_DIRS)
    total_outputs = sum(len(paths) for paths in outputs_files.values())
    print(f"   Total de arquivos em outputs/: {total_outputs}")
    print()

    # 2. Listar arquivos em CONSOLIDADO/
    print("2. Listando arquivos em CONSOLIDADO/...")
    consolidado_files = get_files_in_dir(CONSOLIDADO_DIR, IGNORE_DIRS)
    total_consolidado = sum(len(paths) for paths in consolidado_files.values())
    print(f"   Total de arquivos em CONSOLIDADO/: {total_consolidado}")
    print()

    # 3. Verificar cobertura
    print("3. ANÁLISE DE COBERTURA")
    print("-" * 80)

    copied = []
    not_copied = []
    modified = []
    duplicated_in_consolidado = []

    for filename, output_paths in outputs_files.items():
        # Verificar se existe em CONSOLIDADO
        if filename in consolidado_files:
            # Arquivo existe - verificar se é idêntico
            for output_path in output_paths:
                output_md5 = calculate_md5(output_path)

                # Procurar match de MD5 em CONSOLIDADO
                found_match = False
                for consolidado_path in consolidado_files[filename]:
                    consolidado_md5 = calculate_md5(consolidado_path)
                    if output_md5 == consolidado_md5:
                        copied.append({
                            "filename": filename,
                            "output_path": output_path,
                            "consolidado_path": consolidado_path,
                            "md5": output_md5,
                            "status": "IDENTICAL"
                        })
                        found_match = True
                        break

                if not found_match:
                    # Arquivo existe mas com conteúdo diferente
                    modified.append({
                        "filename": filename,
                        "output_path": output_path,
                        "consolidado_paths": consolidado_files[filename],
                        "output_md5": output_md5,
                        "status": "MODIFIED"
                    })

            # Verificar duplicados em CONSOLIDADO
            if len(consolidado_files[filename]) > 1:
                duplicated_in_consolidado.append({
                    "filename": filename,
                    "paths": consolidado_files[filename]
                })
        else:
            # Arquivo NÃO existe em CONSOLIDADO
            for output_path in output_paths:
                not_copied.append({
                    "filename": filename,
                    "output_path": output_path,
                    "status": "NOT_COPIED"
                })

    # 4. RELATÓRIO DE COBERTURA
    total_unique_files = len(outputs_files)
    total_copied_unique = len([f for f in outputs_files if f in consolidado_files])
    coverage_pct = (total_copied_unique / total_unique_files * 100) if total_unique_files > 0 else 0

    print(f"Total de arquivos ÚNICOS em outputs/: {total_unique_files}")
    print(f"Arquivos copiados para CONSOLIDADO: {total_copied_unique} ({coverage_pct:.1f}%)")
    print(f"Arquivos IDÊNTICOS: {len(copied)}")
    print(f"Arquivos MODIFICADOS: {len(modified)}")
    print(f"Arquivos NÃO COPIADOS: {len(not_copied)}")
    print(f"Arquivos DUPLICADOS em CONSOLIDADO: {len(duplicated_in_consolidado)}")
    print()

    # 5. ARQUIVOS NÃO COPIADOS
    if not_copied:
        print("=" * 80)
        print("ARQUIVOS NÃO COPIADOS (em outputs/ mas NÃO em CONSOLIDADO)")
        print("=" * 80)
        print()

        # Agrupar por categoria
        categorized = {
            "CEP": [],
            "ANVISA": [],
            "TECH_SPECS": [],
            "TESTS": [],
            "ANALYSES": [],
            "MASTER": [],
            "OUTROS": []
        }

        for item in not_copied:
            filename = item["filename"]
            path_str = str(item["output_path"])

            if "PROJ-" in filename or "CRF" in filename or "TCLE" in filename or "OPT_OUT" in filename or "DPIA" in filename:
                categorized["CEP"].append(item)
            elif "ANVISA" in filename or "HDOC_Submission_Package_v2.0" in path_str:
                categorized["ANVISA"].append(item)
            elif any(x in filename for x in ["SRS-001", "SDD-001", "TEC-", "IFU-001", "SEC-001", "RMP-001"]):
                categorized["TECH_SPECS"].append(item)
            elif "test_automation" in path_str or "TEST-" in filename or "BUG-" in filename:
                categorized["TESTS"].append(item)
            elif any(x in filename for x in ["01_", "11_", "15_", "AGENTS_", "STRATEGIC", "RISK"]):
                categorized["ANALYSES"].append(item)
            elif "MASTER" in filename or "INVENTARIO" in filename or "STATUS" in filename or "CONTEXT" in filename:
                categorized["MASTER"].append(item)
            else:
                categorized["OUTROS"].append(item)

        for category, items in categorized.items():
            if items:
                print(f"\n{category} ({len(items)} arquivos):")
                print("-" * 80)
                for item in items:
                    rel_path = item["output_path"].relative_to(OUTPUTS_DIR)
                    print(f"  - {item['filename']}")
                    print(f"    Origem: outputs/{rel_path}")
                    print()

    # 6. ARQUIVOS MODIFICADOS
    if modified:
        print("=" * 80)
        print("ARQUIVOS MODIFICADOS (diferentes checksums)")
        print("=" * 80)
        print()
        for item in modified:
            print(f"Arquivo: {item['filename']}")
            print(f"  Origem: {item['output_path'].relative_to(OUTPUTS_DIR)}")
            print(f"  MD5 (outputs/): {item['output_md5']}")
            print(f"  Destinos em CONSOLIDADO ({len(item['consolidado_paths'])}):")
            for path in item["consolidado_paths"]:
                rel_path = path.relative_to(CONSOLIDADO_DIR)
                md5 = calculate_md5(path)
                print(f"    - {rel_path} (MD5: {md5})")
            print()

    # 7. DUPLICADOS EM CONSOLIDADO
    if duplicated_in_consolidado:
        print("=" * 80)
        print("ARQUIVOS DUPLICADOS EM CONSOLIDADO (mesmo nome, múltiplas localizações)")
        print("=" * 80)
        print()
        for item in duplicated_in_consolidado:
            print(f"Arquivo: {item['filename']}")
            print(f"  Localizações ({len(item['paths'])}):")
            for path in item["paths"]:
                rel_path = path.relative_to(CONSOLIDADO_DIR)
                md5 = calculate_md5(path)
                print(f"    - {rel_path} (MD5: {md5})")
            print()

    # 8. MATRIZ DE MAPEAMENTO (ARQUIVOS COPIADOS)
    print("=" * 80)
    print("MATRIZ DE MAPEAMENTO (Arquivos IDÊNTICOS copiados)")
    print("=" * 80)
    print()
    print(f"{'Arquivo':<50} | {'Origem (outputs/)':<40} | {'Destino (CONSOLIDADO/)'}")
    print("-" * 150)
    for item in copied[:50]:  # Limitar a 50 primeiros
        filename = item["filename"][:48]
        origin = str(item["output_path"].relative_to(OUTPUTS_DIR))[:38]
        dest = str(item["consolidado_path"].relative_to(CONSOLIDADO_DIR))[:60]
        print(f"{filename:<50} | {origin:<40} | {dest}")

    if len(copied) > 50:
        print(f"\n... e mais {len(copied) - 50} arquivos")

    print()

    # 9. AÇÕES CORRETIVAS
    print("=" * 80)
    print("AÇÕES CORRETIVAS RECOMENDADAS")
    print("=" * 80)
    print()

    if not_copied:
        print(f"1. COPIAR {len(not_copied)} ARQUIVOS FALTANTES:")
        print(f"   - CEP: {len(categorized['CEP'])} arquivos")
        print(f"   - ANVISA: {len(categorized['ANVISA'])} arquivos")
        print(f"   - TECH_SPECS: {len(categorized['TECH_SPECS'])} arquivos")
        print(f"   - TESTS: {len(categorized['TESTS'])} arquivos")
        print(f"   - ANALYSES: {len(categorized['ANALYSES'])} arquivos")
        print(f"   - MASTER: {len(categorized['MASTER'])} arquivos")
        print(f"   - OUTROS: {len(categorized['OUTROS'])} arquivos")
        print()

    if modified:
        print(f"2. REVISAR {len(modified)} ARQUIVOS MODIFICADOS:")
        print(f"   - Verificar se modificações são intencionais ou erros")
        print(f"   - Usar diff para comparar diferenças")
        print()

    if duplicated_in_consolidado:
        print(f"3. REMOVER DUPLICADOS: {len(duplicated_in_consolidado)} arquivos duplicados em CONSOLIDADO")
        print(f"   - Manter apenas uma cópia (preferir versão oficial)")
        print()

    print("=" * 80)
    print("FIM DO RELATÓRIO")
    print("=" * 80)

    # Retornar estatísticas
    return {
        "total_outputs": total_outputs,
        "total_unique_outputs": total_unique_files,
        "total_consolidado": total_consolidado,
        "coverage_pct": coverage_pct,
        "copied": len(copied),
        "modified": len(modified),
        "not_copied": len(not_copied),
        "duplicated": len(duplicated_in_consolidado)
    }


if __name__ == "__main__":
    stats = compare_directories()

    # Salvar estatísticas em arquivo
    stats_file = OUTPUTS_DIR.parent / "MIGRATION_COMPARISON_STATS.txt"
    with open(stats_file, "w") as f:
        f.write("ESTATÍSTICAS DE MIGRAÇÃO\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total de arquivos em outputs/: {stats['total_outputs']}\n")
        f.write(f"Arquivos únicos em outputs/: {stats['total_unique_outputs']}\n")
        f.write(f"Total de arquivos em CONSOLIDADO: {stats['total_consolidado']}\n")
        f.write(f"Cobertura: {stats['coverage_pct']:.1f}%\n")
        f.write(f"Arquivos IDÊNTICOS: {stats['copied']}\n")
        f.write(f"Arquivos MODIFICADOS: {stats['modified']}\n")
        f.write(f"Arquivos NÃO COPIADOS: {stats['not_copied']}\n")
        f.write(f"Arquivos DUPLICADOS em CONSOLIDADO: {stats['duplicated']}\n")

    print(f"\nEstatísticas salvas em: {stats_file}")
