---
name: claude-code-helper
description: Generate boilerplate code for HemoDoctor development - YAML parsers, pytest templates, CSV processors, batch processing scripts, and quick stats calculators. Use when starting new modules, writing tests, or automating repetitive tasks. Saves development time and ensures consistent code patterns.
license: Complete terms in LICENSE.txt
---

# Claude Code Helper

Quick code generation for common HemoDoctor development tasks. Generate boilerplate, reduce repetitive work, maintain consistent patterns.

## When to Use This Skill

- **Starting new modules** - Generate YAML parser boilerplate
- **Writing tests** - Generate pytest template with fixtures
- **Data processing** - Convert CSV ↔ JSON, batch processing
- **Quick analysis** - Calculate statistics from test datasets
- **Repetitive tasks** - Automate common patterns

## Quick Start

### Generate YAML Parser

```bash
python scripts/code_helper.py yaml-parser my_parser.py
```

**Output:** Complete YAML parser with load/save functions.

### Generate Pytest Template

```bash
python scripts/code_helper.py pytest test_module.py
```

**Output:** Pytest template with test class, fixtures, edge cases.

### Generate CSV Processor

```bash
python scripts/code_helper.py csv-processor process_csv.py
```

**Output:** CSV to JSON converter with type conversion.

### Generate Batch Processor

```bash
python scripts/code_helper.py batch-processor batch_process.py
```

**Output:** Parallel batch processing with ProcessPoolExecutor.

### Generate Quick Stats

```bash
python scripts/code_helper.py quick-stats calc_stats.py
```

**Output:** Statistics calculator for test datasets.

## Templates

| Template | Purpose | Output |
|----------|---------|--------|
| `yaml-parser` | Parse HemoDoctor YAMLs | Load/save functions, error handling |
| `pytest` | Unit test template | Test class, fixtures, assertions |
| `csv-processor` | CSV ↔ JSON | Type conversion, batch processing |
| `batch-processor` | Parallel processing | ProcessPoolExecutor, progress tracking |
| `quick-stats` | Dataset statistics | Counts, distributions, ranges |

## Template Details

### YAML Parser Template

**Includes:**
- `load_yaml(file_path)` - Safe YAML loading
- `save_yaml(data, file_path)` - Pretty-print saving
- `main()` - CLI with error handling
- UTF-8 encoding support

**Use when:**
- Creating new YAML validators
- Building config loaders
- Implementing YAML transformers

**Example usage of generated code:**
```python
from my_parser import load_yaml

data = load_yaml('03_syndromes_hybrid.yaml')
syndromes = data['syndromes']
```

---

### Pytest Template

**Includes:**
- `TestYourModule` class
- `setup_method()` for fixtures
- `test_basic_functionality()` - Basic test
- `test_edge_case()` - Edge case with pytest.raises
- `test_with_missing_data()` - Missingness handling
- `test_integration()` - Integration test stub

**Use when:**
- Writing unit tests for new modules
- Testing validators
- Testing evidence/syndrome logic

**Example usage of generated code:**
```bash
# Run tests
pytest test_module.py -v

# Run specific test
pytest test_module.py::TestYourModule::test_basic_functionality
```

---

### CSV Processor Template

**Includes:**
- `load_csv(file_path)` - CSV to list of dicts
- `save_csv(data, file_path)` - Dict list to CSV
- Automatic type conversion (string → float)
- None handling for empty values

**Use when:**
- Converting legacy CSV data to JSON
- Importing lab results from Excel
- Batch converting test cases

**Example usage of generated code:**
```bash
# Convert CSV to JSON
python process_csv.py input.csv output.json
```

---

### Batch Processor Template

**Includes:**
- `process_single_case(case)` - Process one case
- `process_batch(cases, max_workers)` - Parallel processing
- ProcessPoolExecutor with progress tracking
- Error handling per case

**Use when:**
- Processing 100s-1000s of test cases
- Running validation on large datasets
- Performance testing

**Example usage of generated code:**
```bash
# Process 500 cases with 8 workers
python batch_process.py cases.json results.json --workers=8
```

---

### Quick Stats Template

**Includes:**
- `calculate_stats(cases)` - Calculate statistics
- Syndrome counts and distributions
- Priority counts
- Numeric field ranges (min/max)

**Use when:**
- Analyzing test datasets
- Validating test case generation
- Quick sanity checks

**Example usage of generated code:**
```bash
python calc_stats.py validation_set.json

# Output:
# Total cases: 500
# By syndrome:
#   S-IDA: 45 (9.0%)
#   S-TMA: 25 (5.0%)
#   NORMAL: 250 (50.0%)
```

## Common Workflows

### Workflow 1: New YAML Validator

```bash
# Generate parser
python scripts/code_helper.py yaml-parser validate_new_yaml.py

# Edit validate_new_yaml.py to add validation logic

# Generate tests
python scripts/code_helper.py pytest test_validate_new_yaml.py

# Edit test_validate_new_yaml.py to add test cases
```

---

### Workflow 2: CSV Import Pipeline

```bash
# Generate CSV processor
python scripts/code_helper.py csv-processor import_csv.py

# Process CSV
python import_csv.py legacy_data.csv imported_cases.json

# Generate stats to verify
python scripts/code_helper.py quick-stats verify_import.py
python verify_import.py imported_cases.json
```

---

### Workflow 3: Batch Testing

```bash
# Generate test cases
python generate_test_cases.py validation 500 cases.json

# Generate batch processor
python scripts/code_helper.py batch-processor run_validation.py

# Edit run_validation.py to add HemoDoctor logic

# Run batch
python run_validation.py cases.json results.json --workers=8

# Generate stats
python scripts/code_helper.py quick-stats analyze_results.py
python analyze_results.py results.json
```

## Customization

All generated templates have TODO comments showing where to add custom logic:

```python
def process_single_case(case: Dict) -> Dict:
    """Process a single case"""
    # TODO: Implement your processing logic
    result = {
        'case_id': case.get('case_id', 'unknown'),
        'input': case,
        'output': None,  # TODO: Add output
        'status': 'success'
    }
    return result
```

**Steps to customize:**
1. Find TODO comments
2. Add your logic
3. Test with sample data
4. Remove TODO comments

## Best Practices

### 1. Always Start with Templates
```bash
# ❌ Don't start from scratch
touch new_module.py

# ✅ Generate template first
python scripts/code_helper.py yaml-parser new_module.py
```

### 2. Generate Tests Immediately
```bash
# After creating module
python scripts/code_helper.py pytest test_new_module.py
```

### 3. Use Batch Processing for Large Datasets
```python
# ❌ Sequential (slow for 500+ cases)
for case in cases:
    process_case(case)

# ✅ Parallel (fast)
python batch_process.py cases.json results.json --workers=8
```

### 4. Verify Imports with Stats
```bash
# After any CSV import
python calc_stats.py imported_data.json
# Check counts match expectations
```

## Integration with Other Skills

### With hemodoctor-validator
```bash
# Generate parser for new YAML
python scripts/code_helper.py yaml-parser parse_new_yaml.py

# Validate it
python scripts/validate_yaml.py new_config.yaml
```

### With clinical-test-generator
```bash
# Generate test cases
python scripts/generate_test_cases.py validation 500 cases.json

# Generate batch processor to run them
python scripts/code_helper.py batch-processor run_cases.py

# Generate stats calculator
python scripts/code_helper.py quick-stats analyze_cases.py
```

### With next-steps-debugger
```bash
# Generate CSV processor for test cases
python scripts/code_helper.py csv-processor convert_tests.py

# Convert CSV to JSON
python convert_tests.py test_cases.csv test_cases.json

# Debug triggers
python scripts/debug_next_steps.py test 09_next_steps.yaml test_cases.json
```

## Examples

### Example 1: Parse Syndrome YAML

```bash
# Generate parser
python scripts/code_helper.py yaml-parser parse_syndromes.py

# Use it
python parse_syndromes.py 03_syndromes_hybrid.yaml
# Output:
# Loaded 4 top-level keys
#   - version
#   - critical_syndromes
#   - priority_syndromes
#   - routine_syndromes
```

### Example 2: Convert Legacy CSV

```bash
# Generate processor
python scripts/code_helper.py csv-processor convert_legacy.py

# Convert
python convert_legacy.py legacy_cases.csv modern_cases.json
# Output:
# Loaded 350 cases
# Saved to modern_cases.json
```

### Example 3: Batch Validation

```bash
# Generate batch processor
python scripts/code_helper.py batch-processor batch_validate.py

# Edit to add validation logic
# ...

# Run
python batch_validate.py cases.json results.json --workers=8
# Output:
# Processing 500 cases with 8 workers...
# Processed 500/500: CASE-500
# Done!
#   Success: 495
#   Errors: 5
```

## Troubleshooting

### Generated Code Has Syntax Errors
- Code is template - review and customize
- Replace TODO comments with actual logic
- Test incrementally

### Import Errors in Generated Code
```bash
# Install missing dependencies
pip install pyyaml  # For yaml-parser
pip install pytest  # For pytest template
```

### Parallel Processing Not Faster
- Check max_workers (default 4)
- Try increasing: `--workers=8` or `--workers=16`
- Ensure tasks are CPU-bound (not I/O-bound)

## Advanced Usage

### Combine Multiple Templates

```bash
# Generate parser
python scripts/code_helper.py yaml-parser my_module.py

# Add batch processing to it manually
# ... copy relevant code from batch-processor template

# Generate tests
python scripts/code_helper.py pytest test_my_module.py
```

### Create Custom Template

Edit `code_helper.py` to add new generator:

```python
def generate_my_template():
    code = '''
#!/usr/bin/env python3
# Your custom template here
'''
    return code

# Add to generators dict
generators = {
    'yaml-parser': generate_yaml_parser,
    'my-template': generate_my_template,  # NEW
    ...
}
```

## Time Savings

| Task | Without Helper | With Helper | Saved |
|------|---------------|-------------|-------|
| YAML parser | 30 min | 2 min | 28 min |
| Pytest template | 15 min | 1 min | 14 min |
| CSV processor | 20 min | 2 min | 18 min |
| Batch processor | 45 min | 5 min | 40 min |
| **Total** | **110 min** | **10 min** | **100 min** |

**ROI:** ~10x time savings on boilerplate tasks.

## Best For

✅ Starting new modules  
✅ Writing repetitive code  
✅ Maintaining consistent patterns  
✅ Quick prototyping  
✅ Batch data processing  

❌ Complex custom logic (use as starting point only)  
❌ One-off scripts (faster to write manually)  

## Resources

- **scripts/code_helper.py** - Main generator with 5 templates
- All templates include TODO comments for customization
- Generated code is production-ready after customization
