#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import click
import logging
from .grafana_dashboard import convert_dashboards, info_dashboards, test_dashboards, metrics_dashboards

logging.basicConfig(
    format="%(asctime)s [%(levelname)-5.5s]  %(message)s",
    level=logging.INFO,
    handlers=[
        logging.StreamHandler()
    ])


@click.command()
@click.option('--source-path', default='./source', help='Path to search for the source JSON dashboards.')
@click.option('--build-path', default='', help='Path to save converted JSONNET dashboards, none to print to console.')
@click.option('--format', default='grafonnet', help='Format of the dashboard: `grafonnet` or `grafana-builder`.')
@click.option('--layout', default='rows',
              help='Format of the dashboard: `normal` (scheme 14) , `grid` (scheme 16).')
def dashboard_convert(source_path, build_path, format, layout):
    """Convert JSON dashboards to JSONNET format."""
    logging.info(
        'Searching path `{}` for JSON dashboards to convert ...'.format(source_path))
    convert_dashboards(source_path, build_path, format, layout)


@click.command()
@click.option('--path', default='./data', help='Path to search for the source JSON dashboards.')
@click.option('--scheme', default='16', help='Scheme version of the dashboard: `16` is the current.')
@click.option('--layout', default='rows',
              help='Format of the dashboard: `normal` (scheme 14) , `grid` (scheme 16).')
def dashboard_test(path, scheme, layout):
    """Test JSONNET formatted dashboards."""
    logging.info(
        'Searching path `{}` for JSON dashboards to test ...'.format(path))
    test_dashboards(path)


@click.command()
@click.option('--path', default='./data', help='Path to search for the source JSON dashboards.')
def dashboard_info(path):
    """Get info from Grafana JSON dashboards."""
    logging.info(
        'Searching path `{}` for JSON dashboards for detailed info ...'.format(path))
    info_dashboards(path)


@click.command()
@click.option('--path', default='./data', help='Path to search for the source JSON dashboards.')
def dashboard_metrics(path):
    """Get metric names from Grafana JSON dashboard targets."""
    logging.info(
        'Searching path `{}` for JSON dashboards for targets ...'.format(path))
    metrics_dashboards(path)
