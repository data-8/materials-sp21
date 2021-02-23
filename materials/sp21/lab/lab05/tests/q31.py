test = {
  'name': 'q31',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.count_nonzero(all_combos.column(1) - all_combos.column(2) == [0, 24]) == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all_combos.column(0).item(0)[0] == "S"
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
