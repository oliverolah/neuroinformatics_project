/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    /**
     * Stylesheet generation mode.
     *
     * Set mode to "jit" if you want to generate your styles on-demand as you author your templates;
     * Set mode to "aot" if you want to generate the stylesheet in advance and purge later (aka legacy mode).
     */
    // mode: "jit", // this is always on in version 3.0 - so there is not use for it atm

    content: [ // this was named PURGE before 3.0 version
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        // '../templates/**/*.html',

        /* 
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        // '../../templates/**/*.html',
        '../../templates/homeroots/home.html',
        '../../templates/footer.html',
        '../../templates/navbar.html',
        '../../templates/submitdata/submit_data_page.html',
        '../../templates/submitdata/submit_data_form.html',
        '../../templates/contactus/contact_us_page.html',
        '../../templates/contactus/contact_us_form.html',
        '../../templates/aboutcontent/about_page.html',
        '../../templates/keysources/key_sources_page.html',
        '../../templates/keysources/key_papers_table.html',
        '../../templates/keysources/key_websites_table.html',
        '../../templates/neurons/visualisations_page.html',
        
        /* 
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        // '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    // darkMode: false, // or 'media' or 'class' - not needed in 3.0
    theme: {
        extend: {},
        // if the 'color{}' below will cause troubles, remove the whole thing
        colors: ({ colors }) => ({
            inherit: colors.inherit,
            current: colors.current,
            transparent: colors.transparent,
            black: colors.black,
            white: colors.white,
            slate: colors.slate,
            gray: colors.gray,
            zinc: colors.zinc,
            neutral: colors.neutral,
            stone: colors.stone,
            red: colors.red,
            orange: colors.orange,
            amber: colors.amber,
            yellow: colors.yellow,
            lime: colors.lime,
            green: colors.green,
            emerald: colors.emerald,
            teal: colors.teal,
            cyan: colors.cyan,
            sky: colors.sky,
            blue: colors.blue,
            indigo: colors.indigo,
            violet: colors.violet,
            purple: colors.purple,
            fuchsia: colors.fuchsia,
            pink: colors.pink,
            rose: colors.rose,
            cardiffMetPrimary: '#002D56',
            cardiffMetPrimaryLighter: '#003566',
            cardiffMetSecondary: '#0D47A1',
            successGreen: '#10A52E',
            successGreenBrighter: '#04C42B'
        }),
    },
    // variants: {
    //     extend: {},
    // }, // variants also not needed in version 3.0
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
