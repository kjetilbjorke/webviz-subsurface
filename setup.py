from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

TESTS_REQUIRE = ["selenium~=3.141", "pylint", "mock", "black", "bandit"]

setup(
    name="webviz-subsurface",
    description="Webviz config containers for subsurface data",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/equinor/webviz-subsurface",
    author="R&T Equinor",
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "webviz_config_containers": [
            "ParameterDistribution = webviz_subsurface.containers:ParameterDistribution",
            "ParameterCorrelation = webviz_subsurface.containers:ParameterCorrelation",
            "DiskUsage = webviz_subsurface.containers:DiskUsage",
            "SubsurfaceMap = webviz_subsurface.containers:SubsurfaceMap",
            "HistoryMatch = webviz_subsurface.containers:HistoryMatch",
            "Intersect = webviz_subsurface.containers:Intersect",
            "MorrisPlot = webviz_subsurface.containers:MorrisPlot",
            "InplaceVolumes = webviz_subsurface.containers:InplaceVolumes",
            "InplaceVolumesOneByOne = webviz_subsurface.containers:InplaceVolumesOneByOne",
            "ReservoirSimulationTimeSeries = "
            + "webviz_subsurface.containers:ReservoirSimulationTimeSeries",
            "ReservoirSimulationTimeSeriesOneByOne = "
            + "webviz_subsurface.containers:ReservoirSimulationTimeSeriesOneByOne",
        ]
    },
    install_requires=[
        "scipy~=1.2",
        "dash-daq~=0.1",
        "matplotlib~=3.0",
        "pillow~=6.1",
        "xtgeo~=2.1",
        "webviz-config>=0.0.24",
        "webviz-subsurface-components>=0.0.3",
    ],
    tests_require=TESTS_REQUIRE,
    extras_require={"tests": TESTS_REQUIRE},
    setup_requires=["setuptools_scm~=3.2"],
    use_scm_version=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Environment :: Web Environment",
        "Framework :: Dash",
        "Framework :: Flask",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
)
