// Docs: https://dbml.dbdiagram.io/docs

Table users {
  id integer [primary key]
  username varchar
  role varchar
  created_at timestamp
}

Table jobs {
  id integer [primary key]
  job_number varchar
  type_id integer
  time_frame varchar
  created_at timestamp
  last_updated timestamp
  notes text
  address_id integer
  user_id integer
}

Table job_types {
  id integer [primary key]
  title varchar
  compensation float
}

Table addresses {
  id integer [primary key]
  address varchar
  created_at timestamp
  last_updated timestamp
}

Table equipments {
  id integer [primary key]
  type varchar
  identefier varchar
  is_return bool
  task_id integer
}

Ref: jobs.user_id > users.id // many-to-one
Ref: jobs.type_id > job_types.id
Ref: jobs.address_id > addresses.id
Ref: equipments.task_id > jobs.id
