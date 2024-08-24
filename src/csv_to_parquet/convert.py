import polars as pl


SCHEMA = {
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


def infer_schema_from_text(text: str) -> dict:
    """
    Infer schema from text

    Args:
        text (str): Schema definition in the format `column1:type1;column2:type2;...`

    Returns:
        dict: Polars-compatible schema definition
    """

    schema = {}
    for schema_definition in text.split(";"):
        column, dtype = schema_definition.split(":")
        dtype = dtype.strip()

        if dtype in SCHEMA:
            schema[column] = SCHEMA[dtype]
        else:
            raise ValueError(
                f"Unknown data type: {dtype}. Types: {', '.join(SCHEMA.keys())}"
            )

    return schema


def convert_csv_to_parquet(input_paths: list[str], parquet_path: str, schema: str = ""):
    """
    Convert CSV to Parquet

    Args:
        input_paths (list[str]): List of CSV file paths
        parquet_path (str): Path to Parquet file
        schema (str, optional): Schema definition. Defaults to ''.

    Raises:
        ValueError: If an unknown data
    """

    if schema:
        schema = infer_schema_from_text(schema)

    individual_frames = [
        pl.read_csv(input_path, schema=schema) for input_path in input_paths
    ]

    df = pl.concat(individual_frames)
    df.write_parquet(parquet_path)
