/**
 * @license Copyright (c) 2003-2017, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	config.uiColor = '#AADC6E';
	config.allowedContent = true;
	config.extraPlugins = 'stylesheetparser';
    fontAwesomeCss = 'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css';
	bootstrapCss = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css';
	mdbCss = 'https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.4.1/css/mdb.css';
    config.stylesSet = [fontAwesomeCss, bootstrapCss, mdbCss];
};
