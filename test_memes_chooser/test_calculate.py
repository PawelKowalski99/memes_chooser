import pytest
import memes_chooser.main


@pytest.mark.parametrize("usb_size, memes, output",
     [
         (1, [('rollsafe.jpg', 205, 6),
              ('sad_pepe_compilation.gif', 410, 10),
              ('yodeling_kid.avi', 605, 12)],
          (22, {'sad_pepe_compilation.gif', 'yodeling_kid.avi'})),

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
              ('duck_face.avi', 635, 11), ],
          (85, {'Deal_With_It.avi', 'homophobic_seal.gif',
                'delete_sys32.avi', 'Leeroy_jenkins.avi',
                'it_is_over_9000.gif'})
          ),
         (1, [('xxxxx.gif', 1, 5),
              ('your_mom_is_gay.png', 2, 3),
              ('doge.jpg', 4, 5),
              ('MLP_friendship_is_magic.mp4', 2, 3),
              ('pepe_frog_depression.png', 5, 2)],
          (18, {'MLP_friendship_is_magic.mp4', 'xxxxx.gif',
                'your_mom_is_gay.png',
                'pepe_frog_depression.png', 'doge.jpg'}))
     ])
def test_calculate(usb_size, memes, output):
    assert output == memes_chooser.main.calculate(usb_size, memes), "test failed"


@pytest.mark.parametrize("usb_size, memes, output",
     [
         (1024, [('Dick_butt.jpg', 205, 6),
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
                 ('duck_face.avi', 635, 11), ],
          (85, 'Leeroy_jenkins.avi homophobic_seal.gif fus_ro_dah.jpg'
               ' it_is_over_9000.gif The_cake_is_a_lie.jpg Ricardo_Milos.gif'
               ' swag.gif duck_face.avi Deal_With_It.avi do_you_even_lift?.gif'
               ' delete_sys32.avi Dick_butt.jpg'))
     ])
def test_inside_calculate(usb_size, memes, output):
    memo_arr = [[[0, []] for _ in range(usb_size + 1)] for _ in range(len(memes) + 1)]
    assert output == memes_chooser.main.inside_calculate(usb_size, memes, memo_arr), "Test Failed"


@pytest.mark.parametrize(" ,usb_size, memes, memes_result,  output",
     [
         (1024, [('Dick_butt.jpg', 205, 6),
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
                 ('duck_face.avi', 635, 11), ],
          ('Leeroy_jenkins.avi homophobic_seal.gif fus_ro_dah.jpg'
           ' it_is_over_9000.gif The_cake_is_a_lie.jpg Ricardo_Milos.gif'
           ' swag.gif duck_face.avi Deal_With_It.avi do_you_even_lift?.gif'
           ' delete_sys32.avi Dick_butt.jpg'),
          ['Deal_With_It.avi', 'homophobic_seal.gif',
           'delete_sys32.avi', 'Leeroy_jenkins.avi',
           'it_is_over_9000.gif'
           ])
     ])
def test_delete_unnecessary_memes(value,
                                  memes_result, memes_original_list, usb_size, output):
    assert output == memes_chooser.main.delete_unnecessary_memes(value,
                                                                 memes_result,
                                                                 memes_original_list,
                                                                 usb_size)
