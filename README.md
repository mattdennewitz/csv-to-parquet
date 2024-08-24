# csv-to-parquet

Schema-aided conversion of CSV data to Parquet format.

## Usage

```shell
csv-to-parquet --schema <schema> --input <input-file> [--input <input-file>...] --output <output-file>
```

## Schema definition

Schemas are supplied via CLI flag, `-s`. This utility exposes a subset of Polars types for schema definition. 

Syntax: `<column-name>:<type>[;<column-name>:<type>...]`

For example, a schema definition for a CSV file with columns `name`, `age`, and `dob` would look like this:
`name:str;age:i32;dob:date`. The full incanation of the CLI command would be:

```shell
csv-to-parquet --schema "name:str;age:i32;dob:date" --input <input-file> --output <output-file>
```

The following types are supported:

```python
{
    "dec": pl.Decimal,
    "i8": pl.Int8,
    "i16": pl.Int16,
    "i32": pl.Int32,
    "i64": pl.Int64,
    "int": pl.Int64,  # Alias for 'i64'
    "u8": pl.UInt8,
    "u16": pl.UInt16,
    "u32": pl.UInt32,
    "u64": pl.UInt64,
    "f32": pl.Float32,
    "f64": pl.Float64,
    "str": pl.Utf8,
    "date": pl.Date,
    "datetime": pl.Datetime,
    "duration": pl.Duration,
    "time": pl.Time,
    "bool": pl.Boolean,
    "null": pl.Null,
}
```