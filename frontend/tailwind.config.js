module.exports = {
  prefix: '',
  purge: {
    content: [
      './src/**/*.{html,ts}',
    ]
  },
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    extend: {
      colors : {
        'light' : '#C8DAFF',
        'dark' : '#8490FC',
        'skin' : '#FF9188',
        'skindark' : '#FF8177'
      },
      textColor : {
        'logo' : '#AD35F8',
      },

      fontFamily : {
        DancingScript: ['Dancing Script'],
        Lobster: ['Lobster', 'cursive'],
        DidactGothic: ['Didact Gothic']
      }

    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
