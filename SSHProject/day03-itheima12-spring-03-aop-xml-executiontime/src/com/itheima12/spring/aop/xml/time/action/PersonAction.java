package com.itheima12.spring.aop.xml.time.action;

import com.itheima12.spring.aop.xml.time.service.PersonService;

public class PersonAction {
	private PersonService personService;

	public PersonService getPersonService() {
		return personService;
	}

	public void setPersonService(PersonService personService) {
		this.personService = personService;
	}
	
	
	public void savePerson(){
		this.personService.savePerson();
	}
}
