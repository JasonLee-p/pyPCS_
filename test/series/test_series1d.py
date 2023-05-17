from __future__ import annotations
import unittest
from pyPCS import Chord
from typing import List


class TestChord(unittest.TestCase):
    C = Chord([60, 64, 67])
    Cm = Chord([60, 63, 67])
    C6 = Chord([60, 64, 67, 69])
    Cm7 = Chord([60, 63, 67, 70])
    Csus2 = Chord([60, 62, 67])
    C57 = Chord([60, 67, 70])
    C56 = Chord([60, 67, 69])
    Csus2sus4 = Chord([60, 62, 65, 67])
    Cadd9 = Chord([60, 62, 64, 67])
    Cmadd11 = Chord([60, 63, 65, 67])
    C6add9 = Chord([60, 62, 64, 67, 69])
    C23 = Chord([60, 62, 64])
    C7 = Chord([60, 64, 67, 70])
    Cm6 = Chord([60, 63, 67, 69])
    Cdim = Chord([60, 63, 66])
    C2s4 = Chord([60, 62, 66])
    C2b6 = Chord([60, 62, 68])
    C9 = Chord([60, 62, 64, 67, 70])
    C23s4 = Chord([60, 62, 64, 66])
    Caug = Chord([60, 64, 68])
    Caugadd9 = Chord([60, 62, 64, 68])  # TODO:
    Caugadd11 = Chord([60, 64, 66, 68])
    C2s4b6 = Chord([60, 62, 66, 68])
    Caugadd9s11 = Chord([60, 62, 64, 66, 68])  # TODO: add11变s11
    Cdim7 = Chord([60, 63, 66, 69])
    C23s4b67 = Chord([60, 62, 64, 66, 68, 70])
    CM7 = Chord([60, 64, 67, 71])
    Cadd11 = Chord([60, 64, 65, 67])
    Cmadd9 = Chord([60, 62, 63, 67])
    CM9 = Chord([60, 62, 64, 67, 71])
    Cm9 = Chord([60, 62, 63, 67, 70])
    C5M7 = Chord([60, 67, 71])
    C5b6 = Chord([60, 67, 68])
    C56M7 = Chord([60, 67, 69, 71])
    C5b67 = Chord([60, 67, 68, 70])
    C567 = Chord([60, 67, 68, 70])
    Cadd9add11 = Chord([60, 62, 64, 65, 67])
    Cmadd9add11 = Chord([60, 62, 63, 65, 67])
    Cm11 = Chord([60, 62, 63, 65, 67, 70])
    C2b3 = Chord([60, 62, 63])
    C2M7 = Chord([60, 62, 71])
    Cs11 = Chord([60, 64, 66, 67])
    Cmb9 = Chord([60, 61, 63, 67])
    C67 = Chord([60, 64, 67, 69, 70])
    Cm67 = Chord([60, 63, 67, 69, 70])
    Cm6add9 = Chord([60, 62, 63, 67, 69])
    C7add11 = Chord([60, 64, 65, 67, 70])
    Csus4M7 = Chord([60, 65, 67, 71])
    Csus2b6 = Chord([60, 62, 67, 68])
    C57b9 = Chord([60, 61, 67, 70])
    C56s11 = Chord([60, 66, 67, 69])
    Cadd9s11 = Chord([60, 62, 64, 66, 67])
    Cmb9add11 = Chord([60, 61, 63, 65, 67])
    C11 = Chord([60, 62, 64, 65, 67, 70])
    Cm11b9 = Chord([60, 61, 63, 65, 67, 70])
    C5b9 = Chord([60, 61, 67])
    C5s11 = Chord([60, 66, 67])
    Cb6 = Chord([60, 64, 67, 68])
    CmM7 = Chord([60, 63, 67, 71])
    Caddb3 = Chord([60, 63, 64, 67])
    Cms11 = Chord([60, 63, 66, 67])
    Cb9 = Chord([60, 61, 64, 67])
    C7b9 = Chord([60, 61, 64, 67, 70])
    Cm6s11 = Chord([60, 63, 66, 67, 69])
    C6addb3 = Chord([60, 63, 64, 67, 69])
    Cm7add3 = Chord([60, 63, 64, 67, 70])
    Cb67 = Chord([60, 64, 67, 68, 70])
    Cm6M7 = Chord([60, 63, 67, 69, 71])
    Cb6add9 = Chord([60, 62, 64, 67, 68])
    CmM7add11 = Chord([60, 63, 65, 67, 71])
    C7s11 = Chord([60, 64, 66, 67, 70])
    Cm6b9 = Chord([60, 61, 63, 67, 69])
    C56b9 = Chord([60, 61, 67, 69])
    C57s11 = Chord([60, 66, 67, 70])
    C3addb3 = Chord([60, 63, 64])
    C3addb9 = Chord([60, 61, 64])
    Cdimadd3 = Chord([60, 63, 64, 66])
    Cdimadd9 = Chord([60, 62, 63, 66])
    C9s11 = Chord([60, 62, 64, 66, 67, 70])
    C9b6 = Chord([60, 62, 64, 67, 68, 70])
    CM7s11 = Chord([60, 64, 66, 67, 71])
    CM7add11 = Chord([60, 64, 66, 67, 71])
    Cdimb9add11 = Chord([60, 61, 63, 65, 66])
    Cm11b5b9 = Chord([60, 61, 63, 65, 66, 70])
    CM11 = Chord([60, 62, 64, 65, 67, 71])
    CM9s11 = Chord([60, 62, 64, 66, 67, 71])
    C5M7s11 = Chord([60, 66, 67, 71])
    CM7addb3 = Chord([60, 63, 64, 67, 71])
    CM7b6 = Chord([60, 64, 67, 68, 71])
    CmM9 = Chord([60, 62, 63, 67, 71])
    Cb6b9 = Chord([60, 61, 64, 67, 68])
    Caddb3s11 = Chord([60, 63, 64, 66, 67])
    Cmaddb3b9 = Chord([60, 61, 63, 64, 67])
    C6M7addb3 = Chord([60, 63, 64, 67, 69, 71])
    Cmb67add3 = Chord([60, 63, 64, 67, 69, 70])
    Cm6M7s11 = Chord([60, 63, 66, 67, 69, 71])
    C11b9 = Chord([60, 61, 64, 65, 67, 70])
    Cm7add3b9 = Chord([60, 61, 63, 64, 67, 70])
    C6addb3s11 = Chord([60, 63, 64, 66, 67, 69])
    C5b6M7 = Chord([60, 67, 68, 71])
    C567b9 = Chord([60, 61, 67, 69, 70])
    C567s11 = Chord([60, 66, 67, 69, 70])
    C2b3M7 = Chord([60, 62, 63, 71])
    Cb67add11 = Chord([60, 64, 65, 67, 68, 70])
    Cm6M9 = Chord([60, 62, 63, 67, 69, 71])
    Cm67b9 = Chord([60, 61, 63, 67, 69, 70])

    def test_colour_tian(self):
        self.assertEqual(TestChord.C.colour_tian, (10, 55.0))
        self.assertEqual(TestChord.Cm.colour_tian, (10, 125.0))
        self.assertEqual(TestChord.C6.colour_tian, (10, 45.0))
        self.assertEqual(TestChord.Cm7.colour_tian, (10, 135.0))
        self.assertEqual(TestChord.Csus2.colour_tian, (9.67, 75.0))
        self.assertEqual(TestChord.C57.colour_tian, (9.67, 115.0))
        self.assertEqual(TestChord.C56.colour_tian, (9.67, 65))
        self.assertEqual(TestChord.Csus2sus4.colour_tian, (9.33, 90.0))
        self.assertEqual(TestChord.Cadd9.colour_tian, (9.33, 52.5))
        self.assertEqual(TestChord.Cmadd11.colour_tian, (9.33, 127.5))
        self.assertEqual(TestChord.C6add9.colour_tian, (9.33, 45.0))
        self.assertEqual(TestChord.C23.colour_tian, (9.33, 45.0))
        self.assertEqual(TestChord.C7.colour_tian, (9, 82.5))
        self.assertEqual(TestChord.Cm6.colour_tian, (9, 97.5))
        self.assertEqual(TestChord.Cdim.colour_tian, (8.67, 75.0))
        self.assertEqual(TestChord.C2s4.colour_tian, (8.67, 25.0))
        self.assertEqual(TestChord.C2b6.colour_tian, (8.67, 125.0))
        self.assertEqual(TestChord.C9.colour_tian, (8.33, 75.0))
        self.assertEqual(TestChord.C23s4.colour_tian, (8.33, 15.0))
        self.assertEqual(TestChord.Caug.colour_tian, (8, 105.0))
        self.assertEqual(TestChord.Caugadd9.colour_tian, (7.67, 90.0))
        self.assertEqual(TestChord.Caugadd11.colour_tian, (7.67, 60.0))
        self.assertEqual(TestChord.C2s4b6.colour_tian, (7.67, 75.0))
        self.assertEqual(TestChord.Caugadd9s11.colour_tian, (7.33, 57.0))
        self.assertEqual(TestChord.Cdim7.colour_tian, (7.33, 60.0))
        self.assertEqual(TestChord.C23s4b67.colour_tian, (7.33, 75.0))
        self.assertEqual(TestChord.CM7.colour_tian, (7, 30.0))
        self.assertEqual(TestChord.Cadd11.colour_tian, (7, 75.0))
        self.assertEqual(TestChord.Cmadd9.colour_tian, (7, 105.0))
        self.assertEqual(TestChord.CM9.colour_tian, (6.67, 33.0))
        self.assertEqual(TestChord.Cm9.colour_tian, (6.67, 117.0))
        self.assertEqual(TestChord.C5M7.colour_tian, (6.33, 45.0))
        self.assertEqual(TestChord.C5b6.colour_tian, (6.33, 135.0))
        self.assertEqual(TestChord.C56M7.colour_tian, (6.33, 37.5))
        self.assertEqual(TestChord.C5b67.colour_tian, (6.33, 142.5))
        self.assertEqual(TestChord.C567.colour_tian, (6.33, 142.5))
        self.assertEqual(TestChord.Cadd9add11.colour_tian, (6.33, 69.0))
        self.assertEqual(TestChord.Cmadd9add11.colour_tian, (6.33, 111.0))
        self.assertEqual(TestChord.Cm11.colour_tian, (6.33, 120.0))
        self.assertEqual(TestChord.C2b3.colour_tian, (6.33, 115.0))
        self.assertEqual(TestChord.C2M7.colour_tian, (6.33, 35.0))
        self.assertEqual(TestChord.Cs11.colour_tian, (6, 22.5))
        self.assertEqual(TestChord.Cmb9.colour_tian, (6, 157.5))
        self.assertEqual(TestChord.C67.colour_tian, (5.67, 69.0))
        self.assertEqual(TestChord.Cm67.colour_tian, (5.67, 111.0))
        self.assertEqual(TestChord.Cm6add9.colour_tian, (5.67, 87.0))
        self.assertEqual(TestChord.C7add11.colour_tian, (5.67, 93.0))
        self.assertEqual(TestChord.Csus4M7.colour_tian, (5.33, 67.5))
        self.assertEqual(TestChord.Csus2b6.colour_tian, (5.33, 112.5))
        self.assertEqual(TestChord.C57b9.colour_tian, (5.33, 150.0))
        self.assertEqual(TestChord.C56s11.colour_tian, (5.33, 30.0))
        self.assertEqual(TestChord.Cadd9s11.colour_tian, (5.33, 27.0))
        self.assertEqual(TestChord.Cmb9add11.colour_tian, (5.33, 153.0))
        self.assertEqual(TestChord.C11.colour_tian, (5.33, 85.0))
        self.assertEqual(TestChord.Cm11b9.colour_tian, (5.33, 155.0))
        self.assertEqual(TestChord.C5b9.colour_tian, (5.33, 145.0))
        self.assertEqual(TestChord.C5s11.colour_tian, (5.33, 35.0))
        self.assertEqual(TestChord.Cb6.colour_tian, (5, 97.5))
        self.assertEqual(TestChord.CmM7.colour_tian, (5, 82.5))
        self.assertEqual(TestChord.Caddb3.colour_tian, (5, 90.0))
        self.assertEqual(TestChord.Cms11.colour_tian, (5, 75.0))
        self.assertEqual(TestChord.Cb9.colour_tian, (5, 105.0))
        self.assertEqual(TestChord.C7b9.colour_tian, (4.67, 117.0))
        self.assertEqual(TestChord.Cm6s11.colour_tian, (4.67, 63.0))
        self.assertEqual(TestChord.C6addb3.colour_tian, (4.67, 75.0))
        self.assertEqual(TestChord.Cm7add3.colour_tian, (4.67, 105.0))
        self.assertEqual(TestChord.Cb67.colour_tian, (4.67, 111.0))
        self.assertEqual(TestChord.Cm6M7.colour_tian, (4.67, 69.0))
        self.assertEqual(TestChord.Cb6add9.colour_tian, (4.67, 87.0))
        self.assertEqual(TestChord.CmM7add11.colour_tian, (4.67, 93.0))
        self.assertEqual(TestChord.C7s11.colour_tian, (4.67, 51.0))
        self.assertEqual(TestChord.Cm6b9.colour_tian, (4.67, 129.0))
        self.assertEqual(TestChord.C56b9.colour_tian, (4.33, 112.5))
        self.assertEqual(TestChord.C57s11.colour_tian, (4.33, 67.5))
        self.assertEqual(TestChord.C3addb3.colour_tian, (4.33, 95.0))
        self.assertEqual(TestChord.C3addb9.colour_tian, (4.33, 115.0))
        self.assertEqual(TestChord.Cdimadd3.colour_tian, (4.33, 52.5))
        self.assertEqual(TestChord.Cdimadd9.colour_tian, (4.33, 67.5))
        self.assertEqual(TestChord.C9s11.colour_tian, (4.33, 50.0))
        self.assertEqual(TestChord.C9b6.colour_tian, (4.33, 100.0))
        self.assertEqual(TestChord.CM7s11.colour_tian, (4, 9.0))
        self.assertEqual(TestChord.CM7add11.colour_tian, (4, 9.0))
        self.assertEqual(TestChord.Cdimb9add11.colour_tian, (3.5, 123.0))
        self.assertEqual(TestChord.Cm11b5b9.colour_tian, (3.5, 130.0))
        self.assertEqual(TestChord.CM11.colour_tian, (3.5, 50.0))
        self.assertEqual(TestChord.CM9s11.colour_tian, (3.5, 15.0))
        self.assertEqual(TestChord.C5M7s11.colour_tian, (3.5, 15.0))
        self.assertEqual(TestChord.CM7addb3.colour_tian, (3, 63.0))
        self.assertEqual(TestChord.CM7b6.colour_tian, (3, 69.0))
        self.assertEqual(TestChord.CmM9.colour_tian, (3, 75.0))
        self.assertEqual(TestChord.Cb6b9.colour_tian, (3, 129.0))
        self.assertEqual(TestChord.Caddb3s11.colour_tian, (3, 57.0))
        self.assertEqual(TestChord.Cmaddb3b9.colour_tian, (3, 123.0))
        self.assertEqual(TestChord.C6M7addb3.colour_tian, (3, 55.0))
        self.assertEqual(TestChord.Cmb67add3.colour_tian, (3, 90.0))
        self.assertEqual(TestChord.Cm6M7s11.colour_tian, (3, 45.0))
        self.assertEqual(TestChord.C11b9.colour_tian, (3, 120.0))
        self.assertEqual(TestChord.Cm7add3b9.colour_tian, (3, 130.0))
        self.assertEqual(TestChord.C6addb3s11.colour_tian, (3, 50.0))
        self.assertEqual(TestChord.C5b6M7.colour_tian, (2.75, 90.0))
        self.assertEqual(TestChord.C567b9.colour_tian, (2.75, 123.0))
        self.assertEqual(TestChord.C567s11.colour_tian, (2.75, 57.0))
        self.assertEqual(TestChord.C2b3M7.colour_tian, (2.75, 75.0))
        self.assertEqual(TestChord.Cb67add11.colour_tian, (2.75, 115.0))
        self.assertEqual(TestChord.Cm6M9.colour_tian, (2.75, 65.0))
        self.assertEqual(TestChord.Cm67b9.colour_tian, (2.75, 135.0))
