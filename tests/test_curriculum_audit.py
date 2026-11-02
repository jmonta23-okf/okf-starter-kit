"""Tests per a l'auditoria curricular (Fase 3 del RFC-OKF-02).

Aquests tests estan en esborrany (skip) fins que el validador implementi
el flag --audit i la lògica de cobertura. Quan arribi la Fase 3, s'implementaran.
"""

import pytest

pytestmark = pytest.mark.skip(reason="Fase 3 del RFC-OKF-02: pendent d'implementació")


def test_audit_cobertura_completa():
    """Una AEA que declara tots els CAs del catàleg dona cobertura 100%."""
    pass


def test_audit_criteri_inexistent():
    """Una AEA que declara un CA que no és al catàleg dona error."""
    pass


def test_audit_criteri_orfes():
    """Un CA del catàleg sense cap AEA que l'avaluï dona warning."""
    pass


def test_audit_sintesi_no_compta():
    """Una AEA amb naturalesa: sintesi no compta per a la cobertura de primer ordre."""
    pass


def test_audit_mismatch_versio():
    """Una AEA amb cataleg_versio diferent del catàleg dona warning (o error amb --strict-versio)."""
    pass


def test_audit_coherencia_yaml_ancora():
    """Un CA al frontmatter sense àncora al cos dona error."""
    pass


def test_audit_instrument_per_criteri():
    """Un CA sense instrument associat dona warning."""
    pass