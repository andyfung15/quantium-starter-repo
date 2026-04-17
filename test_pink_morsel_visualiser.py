from pink_morsel_visualiser import dash_app

def collect_ids(component):
    ids = set()

    if hasattr(component, "id") and component.id is not None:
        ids.add(component.id)

    children = getattr(component, "children", None)

    if isinstance(children, list):
        for child in children:
            if child is not None:
                ids.update(collect_ids(child))
    elif children is not None:
        ids.update(collect_ids(children))

    return ids

def test_header_present():
    ids = collect_ids(dash_app.layout)
    assert "header" in ids

def test_visualisation_present():
    ids = collect_ids(dash_app.layout)
    assert "visualization" in ids

def test_region_picker_present():
    ids = collect_ids(dash_app.layout)
    assert "region_picker" in ids