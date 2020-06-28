var gulp = require('gulp');
var $ = require('gulp-load-plugins')();

gulp.task('compile', done => {
  gulp.src('/sass/**/*.scss')
    .pipe($.plumber())
    .pipe($.sass())
    .pipe($.pleeease({
      minifier: true,
    }))
    .pipe(gulp.dest('/css'))
    done()
});