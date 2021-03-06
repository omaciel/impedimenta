# coding=utf-8
"""Manage Movie Recommender data sets."""
import argparse

from movie_recommender.constants import DATASETS
from movie_recommender.datasets import Dataset, get_installed_datasets


def main():
    """Parse arguments and call business logic."""
    # The `dest` argument is a workaround for a bug in argparse. See:
    # https://stackoverflow.com/questions/23349349/argparse-with-required-subparser
    parser = argparse.ArgumentParser(
        description='Manage Movie Recommender data sets.',
    )
    subparsers = parser.add_subparsers(dest='subcommand', required=True)
    add_absent_subcommand(subparsers)
    add_install_subcommand(subparsers)
    add_present_subcommand(subparsers)
    args = parser.parse_args()
    args.func(args)


def add_absent_subcommand(subparsers):
    """Add the absent subcommand to an argparse subparsers object."""
    helptext = "List datasets which aren't installed."
    parser = subparsers.add_parser(
        'absent',
        help=helptext,
        description=helptext,
    )
    parser.set_defaults(func=handle_absent)


def add_install_subcommand(subparsers):
    """Add the install subcommand to an argparse subparsers object."""
    parser = subparsers.add_parser(
        'install',
        help='Install a dataset.',
        description="""\
        Install a dataset. If the source archive hasn't yet been downloaded
        (with the "download" subcommand), it will automatically be downloaded.
        """,
    )
    parser.add_argument(
        'dataset',
        help='The dataset to install.',
        choices=DATASETS.keys(),
    )
    parser.set_defaults(func=handle_install)


def add_present_subcommand(subparsers):
    """Add the present subcommand to an argparse subparsers object."""
    helptext = 'List installed datasets.'
    parser = subparsers.add_parser(
        'present',
        help=helptext,
        description=helptext,
    )
    parser.add_argument(
        '--paths',
        help='List the paths to the datasets, instead of their names.',
        action='store_true',
    )
    parser.set_defaults(func=handle_present)


def handle_absent(_):
    """Handle the "absent" subcommand."""
    datasets = get_installed_datasets()
    absent_dataset_names = set(DATASETS.keys()) - set(datasets.keys())
    for absent_dataset_name in absent_dataset_names:
        print(absent_dataset_name)


def handle_install(args):
    """Handle the "install" subcommand."""
    dataset = Dataset(args.dataset)
    dataset.download()
    dataset.install()


def handle_present(args):
    """Handle the "present" subcommand."""
    datasets = get_installed_datasets()
    if args.paths:
        for dataset_path in datasets.values():
            print(dataset_path)
    else:
        for dataset_name in datasets:
            print(dataset_name)
