module.exports = function(grunt) {
  grunt.initConfig({
    sass: {
      dsass: {
        files: {
          "base/static/css/styles.css": "assets/scss/styles.scss",
        }
      }
    },
    watch: {
      options: {
        livereload: true
      },
      css: {
        files: ['base/static/css/*.css']
      },
      sass: {
        files: ['assets/scss/*.scss'], // which files to watch
        tasks: ['sass'],
        options: {
          livereload: false
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['watch']);
};
