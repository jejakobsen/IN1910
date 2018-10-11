from exp_decay import ExponentialDecay
import nose.tools as nt

def test_ExponentialDecay():
    main = ExponentialDecay(0.4)
    call = main(0,3.2)
    nt.assert_equal(call, -1.28)

test_ExponentialDecay()

if __name__ == "__main__":
    import nose
    nose.run()
