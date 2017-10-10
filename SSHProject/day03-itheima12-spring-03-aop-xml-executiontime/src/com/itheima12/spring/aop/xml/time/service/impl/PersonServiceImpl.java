package com.itheima12.spring.aop.xml.time.service.impl;

import com.itheima12.spring.aop.xml.time.dao.PersonDao;
import com.itheima12.spring.aop.xml.time.service.PersonService;

public class PersonServiceImpl implements PersonService{
	private PersonDao personDao;

	public PersonDao getPersonDao() {
		return personDao;
	}

	public void setPersonDao(PersonDao personDao) {
		this.personDao = personDao;
	}

	public void savePerson() {
		this.personDao.savePerson();
	}
}	
