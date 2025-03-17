theme = gr.themes.Soft(
    primary_hue=gr.themes.Color(c100="#ffe7d6", c200="#ffdbc2", c300="#ffcfad", c400="#ffc499", c50="#fff3eb", c500="#FFB17A", c600="#ffac70", c700="#ffa05c", c800="#ff9447", c900="#ff9433", c950="#ff7c1f"),
    secondary_hue=gr.themes.Color(c100="#e0e7ff", c200="#c7d2fe", c300="#a5b4fc", c400="#818cf8", c50="rgba(255, 255, 255, 1)", c500="#6366f1", c600="#4f46e5", c700="#4338ca", c800="#3730a3", c900="#312e81", c950="#2b2c5e"),
    neutral_hue=gr.themes.Color(c100="#585c89", c200="#5f6595", c300="#585c89", c400="#50547c", c50="#5f6595", c500="#424668", c600="#404364", c700="#383b57", c800="#30324b", c900="#164e63", c950="#14455c"),
    font=[gr.themes.GoogleFont('Poppins'), 'sans-serif', 'system-ui', 'sans-serif'],
    font_mono=[gr.themes.GoogleFont('poppins-regular'), 'ui-monospace', 'Consolas', 'monospace'],
).set(
    body_background_fill='*primary_800',
    body_background_fill_dark='*neutral_700',
    body_text_color='*neutral_700',
    body_text_color_dark='*secondary_50',
    body_text_color_subdued='*primary_300',
    body_text_color_subdued_dark='*secondary_50',
    background_fill_primary='*primary_300',
    background_fill_primary_dark='*neutral_800',
    background_fill_secondary='*neutral_300',
    background_fill_secondary_dark='*neutral_500',
    border_color_accent_subdued='*secondary_700',
    color_accent_soft='*primary_300',
    link_text_color='*neutral_50',
    link_text_color_dark='*secondary_50',
    link_text_color_active='*secondary_50',
    link_text_color_active_dark='*secondary_50',
    link_text_color_hover_dark='*secondary_50',
    link_text_color_visited_dark='*neutral_50',
    code_background_fill_dark='*secondary_50',
    block_background_fill='*primary_50',
    block_info_text_color='*neutral_50',
    block_info_text_color_dark='*secondary_50',
    block_label_text_color='*neutral_700',
    block_label_text_color_dark='*secondary_50',
    block_title_text_color_dark='*neutral_800',
    loader_color='*primary_300',
    button_large_radius='*radius_xxl',
    button_small_radius='*radius_xxl',
    button_small_text_weight='600',
    button_medium_radius='*radius_xxl',
    button_primary_background_fill_hover='*primary_600',
    button_primary_background_fill_hover_dark='*primary_900',
    button_primary_text_color='*primary_800',
    button_primary_text_color_dark='*neutral_700',
    button_secondary_background_fill_dark='*neutral_400',
    button_secondary_border_color_hover='*neutral_600',
    button_secondary_border_color_hover_dark='*neutral_900',
    button_secondary_text_color_hover_dark='*neutral_800'
)
__all__ = ["theme"]
