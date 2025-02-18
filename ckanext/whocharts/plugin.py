import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class WhochartsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IResourceView, inherit=True)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "whocharts")

    # IResourceView
    
    def info(self):
        return {
            'name': 'portal_map',
            'title': 'Portal Map',
            'icon': 'chart-bar',
            'iframed': False,
            'default_title': 'Portal Map',
            'always_available': True,
            'preview_enabled': True,
            'full_page_edit': False,
        }
    
    def can_view(self, data_dict):
        """
        Determine if this view is applicable for the given resource.
        We want to enable this view for CSV and Excel files.
        """
        resource = data_dict['resource']
        format = resource.get('format', '').lower()
        return format in ['csv', 'xls', 'xlsx']
    
    def view_template(self, context, data_dict):
        return 'views/portal_map.html'
    
    def view_config(self, context, data_dict):
        """
        Optionally pass additional configuration variables to your template.
        """
        return {}
    
    def order(self):
        """
        Determines the display order if multiple resource views are available.
        """
        return 1