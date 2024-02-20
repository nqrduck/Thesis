 # Masterproject

This repository contains the thesis for the NQRduck project. The NQRduck project is a software for controlling a nuclear quadrupole resonance (NQR) and nuclear magnetic resonance (NMR) spectrometer. The project is mostly written in Python and uses the PyQt6 library for the graphical user interface. You can find the NQRduck project at [NQRduck](https://github.com/nqrduck). The source code that was developed in the course of the thesis is tagged with 'Masterproject'.

However since the writing of the thesis the project has been changed in several ways. E.g. the LimeSDR module now uses python bindings for the communication with the SDR. The thesis is therefore not up to date with the current state of the project.

The Latex source code of the Thesis is not included in this repository. I did however include the scripts for data processing and the figures used in the thesis (at least the ones i created).

## Abstract
Recent developments in open-source Software Defined Radio (SDR) have enabled the creation of low-cost spectrometers for magnetic resonance applications.

This thesis describes a modular framework for magnetic resonance experiments for didactic purposes using SDR-based spectrometers. It covers the different hardware implementations conducted in the course of this Master’s project and gives an overview over their functionality. 

Additionally, the thesis introduces NQRduck, a software tool developed during this Master’s project. NQRduck is a modular Python framework designed for conducting magnetic resonance experiments. Its architecture allows independent development and installation of modules. The thesis outlines modules used for tuning and matching of probe coils, pulse programming for SDR spectrometers, and executing single frequency and broadband experiments.

The Results section showcases the different functionalities implemented in the course of this project.

Finally, the various limitations and potential future implementations for the NQRduck software and hardware implementations are discussed.

Keywords: Open Source, Magnetic Resonance, Python, Software Defined Radio, Automatic Tuning and Matching


