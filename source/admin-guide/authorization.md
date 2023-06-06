# Authorization

The authorization management page is the place where an administrator can handle domains, roles and privileges for users.

## Domain

A Domain is an organizational unit to regroup User, Group and Objects (Entity). It also contains the Thematic Communities.
When a user is member of a domain, he can access entities which belong to this domain, according to the provileges defined in his role.

The kind of a domain can be:

- USER: the domain is the private domain of the user
- GROUP: the domain is private to a group of users
- PRIVATE: the domain is a private community (user can only join by invitation)
- PUBLIC: the domain is a public community (all can join)

## Roles

A Role defines the set of privileges that are granted to a User or a Group for a specific Domain or globally.
A Privilege is an access control for a given entity (object) type. For all objects, there are 6 basic privileges : "Can Create", "Can Change", "Can Delete", "Can View", "Can Search", "Can Manage" and "Make Public". For instance, "Can Create" for Series specify the possibility to create a data collection in the system.

From this tab, the administrator can for the selected role add or remove privileges.

:::{figure} ../includes/role_priv.png
:align: center
:figclass: img-container-border
:scale: 50%
:::

## Rolegrant

The assignement of a Role to a User or a Group is called a "Role Grant". A Role Grant can be associated to a Domain and is therefore called "Domain Role Grant". A Role Grant not associated to any domain is a "Global Role Grant".

From this tab, the administrator must first select a domain and then can see all existing role grants, add new ones or delete existing ones.
