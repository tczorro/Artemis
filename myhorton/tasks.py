from __future__ import absolute_import
from celery import shared_task
from horton import *

@shared_task
def hf_calculation(mol_path, basis, alpha, beta, scf):
    mol = IOData.from_file(mol_path)
    obasis = get_gobasis(mol.coordinates, mol.numbers, basis)
    lf = DenseLinalgFactory(obasis.nbasis)
    olp = obasis.compute_overlap(lf)
    kin = obasis.compute_kinetic(lf)
    na = obasis.compute_nuclear_attraction(mol.coordinates, mol.pseudo_numbers, lf)
    er = obasis.compute_electron_repulsion(lf)

    # Create alpha orbitals
    exp_alpha = lf.create_expansion()
    exp_beta = lf.create_expansion()

    # Initial guess
    guess_core_hamiltonian(olp, kin, na, exp_alpha, exp_beta)

    # Construct the restricted HF effective Hamiltonian
    external = {'nn': compute_nucnuc(mol.coordinates, mol.pseudo_numbers)}
    terms = [
        UTwoIndexTerm(kin, 'kin'),
        UDirectTerm(er, 'hartree'),
        UExchangeTerm(er, 'x_hf'),
        UTwoIndexTerm(na, 'ne'),
    ]
    ham = UEffHam(terms, external)

    # Decide how to occupy the orbitals (5 alpha electrons, 4 beta electrons)
    occ_model = AufbauOccModel(alpha, beta)
    if scf == "plain_scf":
        scf_solver = PlainSCFSolver(1e-6)
    scf_solver(ham, lf, olp, occ_model, exp_alpha, exp_beta)