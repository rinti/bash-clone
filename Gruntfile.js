module.exports = function(grunt) {
  grunt.initConfig({
    sass: {
      dsass: {
        files: {
          "base/static/css/styles.css": "assets/scss/styles.scss",
        }
      }
    },
    uglify: {
      dist: {
        files: {
          'base/static/js/scripts.js': ['assets/js/scripts.js']
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
      js: {
        files: ['assets/js/*.js'],
        tasks: ['uglify']
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
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.registerTask('default', ['watch']);
};
