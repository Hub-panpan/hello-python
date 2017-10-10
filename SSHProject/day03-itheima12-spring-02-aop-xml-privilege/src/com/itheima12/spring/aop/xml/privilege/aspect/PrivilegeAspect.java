package com.itheima12.spring.aop.xml.privilege.aspect;

import java.util.ArrayList;
import java.util.List;

import org.aspectj.lang.ProceedingJoinPoint;

import com.itheima12.spring.aop.xml.privilege.annotation.AnnotationParse;
import com.itheima12.spring.aop.xml.privilege.bean.Privilege;

public class PrivilegeAspect {
	/**
	 * 用户拥有的权限 privileges
	 */
	private List<Privilege> privileges = new ArrayList<Privilege>();
	
	public List<Privilege> getPrivileges() {
		return privileges;
	}

	public void setPrivileges(List<Privilege> privileges) {
		this.privileges = privileges;
	}

	public void isAccessMethod(ProceedingJoinPoint joinPoint) throws Throwable{
		/**
		 * 1、获取访问目标方法应该具备的权限
		 *     得到
		 *        1、目标类的class形式
		 *        2、方法的名称
		 */
		Class targetClass = joinPoint.getTarget().getClass();
		//连接点就是个方法  实际上是得到一个方法 访问该 方法的权限
		String methodName = joinPoint.getSignature().getName();
		//得到访问该方法的权限
		
		//得到两个参数    
		String methodAccess = AnnotationParse.parse(targetClass, methodName);
		boolean flag = false;//做个标记
		
		
		
		//遍历用户所有的权限，查看是否用访问该方法的权限
		for (Privilege privilege : privileges) {
			//该用户能够访问目标方法 也就是用户是拥有权限 能够访问目标方法
			
			if(methodAccess.equals(privilege.getName())){
				flag = true;
			}
		}
		
		if(flag){//访问目标方法
			//怎么放行
			//切入点表达式扩展多大 就能写多大
			joinPoint.proceed();
		}else{
			//否则就是没有这个权限
			System.out.println("对不起，您没有权限访问");
		}
	}
}
