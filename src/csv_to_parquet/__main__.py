import click

from .convert import convert_csv_to_parquet


@click.group()
def cli(): ...


@cli.command("convert")
@click.option(
    "-i",
    "--input-path",
    'input_paths',
    help="Input CSV file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    multiple=True,
)
@click.option(
    "-o",
    "--output-path",
    help="Output Parquet file",
    type=click.Path(file_okay=True, dir_okay=False),
)
@click.option(
    "-s",
    "--schema",
    help="Schema definition",
    type=str,
    default="",
)
def run_conversion(input_paths: list[str], output_path: str, schema: str):
    convert_csv_to_parquet(input_paths, output_path, schema)


if __name__ == "__main__":
    cli()
