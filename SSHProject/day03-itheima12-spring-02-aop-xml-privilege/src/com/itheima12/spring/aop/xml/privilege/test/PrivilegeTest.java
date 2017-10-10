package com.itheima12.spring.aop.xml.privilege.test;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.itheima12.spring.aop.xml.privilege.aspect.PrivilegeAspect;
import com.itheima12.spring.aop.xml.privilege.bean.Privilege;
import com.itheima12.spring.aop.xml.privilege.service.PersonService;

public class PrivilegeTest {
	@Test
	public void testPrivilege(){
		//首先 得启动容器
		ApplicationContext context = 
			new ClassPathXmlApplicationContext("applicationContext.xml");
		/**
		 * 初始化用户的权限
		 * 这个就是模仿的 web界面 如果是Web界面这些就不用写了
		 * 权限和业务逻辑一丁点关系都没有关系 我就是通过AOP来配置的
		 */
		
		//先把权限拿出来 初始化用户 的权限
		PrivilegeAspect privilegeAspect = (PrivilegeAspect)context.getBean("privilegeAspect");
		Privilege privilege1 = new Privilege();
		//设置用户权限
		privilege1.setName("savePerson");
		
		Privilege privilege2 = new Privilege();
		privilege2.setName("updatePerson");
		//写一下两天语句  这样的话初始化就完毕了
		privilegeAspect.getPrivileges().add(privilege2);
		privilegeAspect.getPrivileges().add(privilege1);
		
		PersonService personService = (PersonService)context.getBean("personService");
		personService.savePerson();
		//personService.updatePerson();
	}
}
