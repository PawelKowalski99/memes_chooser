import pytest
from main import calculate
import logging


@pytest.mark.parametrize("usb_size, memes, result",
                         [
                             (1, [('Dick_butt.jpg', 205, 6),
                                  ('do_you_even_lift?.gif', 410, 10),
                                  ('Deal_With_It.avi', 126, 11),
                                  ('Ricardo_Milos.gif', 584, 20),
                                  ('homophobic_seal.gif', 320, 25),
                                  ('delete_sys32.avi', 175, 16),
                                  ('fus_ro_dah.jpg', 105, 10),
                                  ('it_is_over_9000.gif', 210, 19),
                                  ('Leeroy_jenkins.avi', 105, 14),
                                  ('The_cake_is_a_lie.jpg', 265, 9),
                                  ('swag.gif', 320, 15),
                                  ('duck_face.avi', 635, 11)],
                              (85, {'Deal_With_It.avi', 'homophobic_seal.gif',
                                    'delete_sys32.avi', 'Leeroy_jenkins.avi',
                                    'it_is_over_9000.gif'})
                              ),
                             (1, [('rollsafe.jpg', 205, 6),
                                  ('sad_pepe_compilation.gif', 410, 10),
                                  ('yodeling_kid.avi', 605, 12)],
                              (22, {'sad_pepe_compilation.gif', 'yodeling_kid.avi'})
                              ),
                             (1, [], logging.error("There are no memes inside list or usb size is <= 0")),
                             (0, [('rollsafe.jpg', 205, 6),
                                  ('sad_pepe_compilation.gif', 410, 10),
                                  ('yodeling_kid.avi', 605, 12)],
                              logging.error("There are no memes inside list or usb size is <= 0")),
                             (-2, [('rollsafe.jpg', 205, 6),
                                   ('sad_pepe_compilation.gif', 410, 10),
                                   ('yodeling_kid.avi', 605, 12)],
                              logging.error("There are no memes inside list or usb size is <= 0"))
                         ])
def test_calculate(usb_size, memes, result):
    assert result == calculate(usb_size, memes)
